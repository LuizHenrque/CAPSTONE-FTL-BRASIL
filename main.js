eox-storytelling id="markdown-globe-tour"></eox-storytelling>

<script type="module">
  import "@eox/storytelling/dist/eox-storytelling.js";

  const eoxStorytelling = document.querySelector("eox-storytelling");

  // Assign properties
  Object.assign(eoxStorytelling, {
    markdown:
      '## Map Tour section <!--{ as="eox-map" class="overlay-br" mode="tour" }-->\nLorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quos. <!--{ style="opacity: 0.75; font-size: 1rem;" }-->\n\n### <!--{ projection="globe" layers=\'[{"type":"Tile","properties":{"id":"osm"},"source":{"type":"OSM"}}]\' center=[12.46,41.89] zoom="5" animationOptions="{duration:500}" }-->\n#### This is a map tour.\nIt allows you to have different layers, zoom and center settings for each tour "step".\n\nYou achieve this by starting a new step with an *h3* (*###*) heading and passing properties inside a configuration comment:\n\n```markdown\n### <!--{ projection="globe" layers=\'[...]\' center=[12.46,41.89] zoom="5" animationOptions="{duration:500}" }-->\n```\n\n### <!--{ projection="globe" layers=\'[{"type":"Tile","properties":{"id":"customId"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2017"}},{"type":"Tile","properties":{"id":"osm"},"source":{"type":"OSM"}}]\' center=[12.46,41.89] zoom="10" animationOptions="{duration:500}" }-->\n#### Second tour step.\nEach tour step is described as an *h3* (*###*) heading.\n\n### <!--{ projection="globe" layers=\'[{"type":"Tile","properties":{"id":"customId"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2017"}}, {"type":"Tile","properties":{"id":"osm"},"source":{"type":"OSM"}}]\' center="[16.36,48.2]" zoom="15" animationOptions="{duration:1000, pitch:-120}" }-->\n#### Third tour step.\n\n### <!--{ projection="globe" layers=\'[{"type":"Tile","properties":{"id":"customId"},"source":{"type":"WMTSCapabilities","url":"https://tiles.maps.eox.at/wmts/1.0.0/WMTSCapabilities.xml","layer":"s2cloudless-2017"}}, {"type":"Tile","properties":{"id":"osm"},"source":{"type":"OSM"}}]\' center="[16.36,48.2]" zoom="15" animationOptions="{duration:1000,}" }-->\n#### Fourth tour step.\n\nTo change individual parameters like zoom or center, or to change the map layers for a step, just set them using the HTML comment syntax. This changes the map setting for the current map',
    showNav: true,
  });
</script>