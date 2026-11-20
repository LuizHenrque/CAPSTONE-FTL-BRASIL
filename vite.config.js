import { defineConfig } from "vite";

export default defineConfig({
  // Relative base so the site works under https://<user>.github.io/<repo>/ (and on forks) without hard-coding the repo name
  base: "./",
  build: {
    // Keep Vite's bundles out of dist/assets/, which holds the story's images and data (copied by `npm run build`)
    assetsDir: "_app",
    // @eox/map + OpenLayers produce a ~5 MB main chunk; that's expected for this page
    chunkSizeWarningLimit: 6000,
  },
});
