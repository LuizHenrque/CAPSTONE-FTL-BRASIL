"""
Download NOAA OISST v2.1 sea surface temperature ANOMALY maps of the tropical Pacific
from NOAA CoastWatch ERDDAP (griddap) and save them as PNG images for the story.

Dataset : NOAA OISST v2.1, daily, 0.25 deg  (ERDDAP dataset id: ncdcOisst21Agg)
Variable: anom  (daily SST anomaly vs. the 1991-2020 climatology, degree C)
Server  : https://coastwatch.pfeg.noaa.gov/erddap

The images are rendered by ERDDAP itself (".png" output), including coastlines/land,
axes and a colour bar, so they can be used directly in the eox-storytelling image tour.

Usage (from the project root):
    python3 studies/fetch_oisst_anom.py
    python3 studies/fetch_oisst_anom.py --dates 2026-07-01 2026-09-01 2026-11-02
    python3 studies/fetch_oisst_anom.py --vmin -4 --vmax 4 --width 1800 --height 800

Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ERDDAP = "https://coastwatch.pfeg.noaa.gov/erddap"
DATASET = "ncdcOisst21Agg"  # longitudes 0..360, so the Pacific is one continuous box
VARIABLE = "anom"

# Tropical Pacific: 120E (Indonesia) -> 290E = 70W (South American coast), 30S..30N.
# This covers the Nino 3.4 box (5S-5N, 170W-120W) and the coast of Peru/Ecuador.
DEFAULT_LAT = (-30.0, 30.0)
DEFAULT_LON = (120.0, 290.0)

# Three dates showing how the 2026 El Nino develops (OISST has ~2 weeks latency).
DEFAULT_DATES = ["2026-07-01", "2026-09-01", "2026-11-02"]

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = PROJECT_ROOT / "assets" / "oisst"


def build_url(date: str, lat: tuple[float, float], lon: tuple[float, float],
              vmin: float, vmax: float, width: int, height: int) -> str:
    """Build an ERDDAP griddap .png request for one day of SST anomaly."""
    # griddap constraint: anom[(time)][(zlev)][(lat0):(lat1)][(lon0):(lon1)]
    query = (
        f"{VARIABLE}"
        f"[({date}T12:00:00Z)]"
        f"[(0.0)]"
        f"[({lat[0]}):({lat[1]})]"
        f"[({lon[0]}):({lon[1]})]"
    )
    options = {
        ".draw": "surface",
        ".vars": f"longitude|latitude|{VARIABLE}",
        # palette | continuity (C=continuous) | scale | min | max | nSections
        ".colorBar": f"BlueWhiteRed|C|Linear|{vmin}|{vmax}|{int((vmax - vmin) * 2)}",
        ".land": "over",          # draw land and coastlines on top of the data
        ".bgColor": "0xffffffff",  # opaque white background
        ".size": f"{width}|{height}",
    }
    return (
        f"{ERDDAP}/griddap/{DATASET}.png?"
        f"{urllib.parse.quote(query, safe='')}&{urllib.parse.urlencode(options)}"
    )


def download(url: str, target: Path, retries: int = 3, timeout: int = 180) -> int:
    """Download url to target with simple retries. Returns the number of bytes written."""
    request = urllib.request.Request(url, headers={"User-Agent": "el-nino-story/1.0"})
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                content_type = response.headers.get("Content-Type", "")
                data = response.read()
            if not content_type.startswith("image/png"):
                raise RuntimeError(f"unexpected response ({content_type}): {data[:300]!r}")
            target.write_bytes(data)
            return len(data)
        except (urllib.error.URLError, TimeoutError, RuntimeError) as error:
            # ERDDAP returns HTTP 404 "Your query produced no matching results" for dates
            # that are not available yet; no point retrying client errors (4xx).
            # Server errors (5xx, e.g. 503 "Wait a minute, then try again") are retried.
            if isinstance(error, urllib.error.HTTPError) and (error.code < 500 or attempt == retries):
                body = error.read().decode("utf-8", "replace")
                raise RuntimeError(f"HTTP {error.code}: {body.strip()[:300]}") from None
            if attempt == retries:
                raise
            wait = 20 * attempt
            print(f"    attempt {attempt} failed ({error}); retrying in {wait}s", file=sys.stderr)
            time.sleep(wait)
    raise AssertionError("unreachable")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dates", nargs="+", default=DEFAULT_DATES, help="dates as YYYY-MM-DD")
    parser.add_argument("--vmin", type=float, default=-3.0, help="colour bar minimum (degree C)")
    parser.add_argument("--vmax", type=float, default=3.0, help="colour bar maximum (degree C)")
    parser.add_argument("--width", type=int, default=1600, help="image width in pixels")
    parser.add_argument("--height", type=int, default=700, help="image height in pixels")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="output folder")
    args = parser.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    failures = 0
    for date in args.dates:
        url = build_url(date, DEFAULT_LAT, DEFAULT_LON, args.vmin, args.vmax, args.width, args.height)
        target = args.out / f"oisst_anom_{date}.png"
        print(f"{date}: {url}")
        try:
            size = download(url, target)
            print(f"    saved {target.relative_to(PROJECT_ROOT) if target.is_relative_to(PROJECT_ROOT) else target} ({size / 1024:.0f} KB)")
        except Exception as error:  # keep going with the other dates
            failures += 1
            print(f"    FAILED: {error}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
