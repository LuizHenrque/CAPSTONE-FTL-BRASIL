import { copyFileSync, cpSync } from "node:fs";

copyFileSync("elnino.md", "dist/elnino.md");
cpSync("assets", "dist/assets", { recursive: true });
