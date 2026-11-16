// The Dossier ($DOSSIER) — makefun-coin-promo-01 entrypoint, round 5.
// Offline only: copies the coin launch record (LAUNCH.json) from the
// repository into the output directory. No network, no signing, no RPC,
// no keypair — the coin is created on pump.fun in a separate step, and
// this file only hands its launch record to the grader.
//
// The entry is the coin itself: the house reads it as pump.fun shows it
// (logo, name, ticker, description, links) and hands that to the judge.
// Nothing this program writes about the coin is judged.
import fs from "node:fs";
import path from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR || "/bot";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";

function main() {
  const sourcePath = path.join(botDir, "LAUNCH.json");
  const targetPath = path.join(outputDir, "LAUNCH.json");
  try {
    fs.mkdirSync(outputDir, { recursive: true });
    fs.copyFileSync(sourcePath, targetPath);
  } catch (err) {
    console.error("DOSSIER: could not copy LAUNCH.json: " + err.message);
    process.exit(1);
  }
  let record;
  try {
    record = JSON.parse(fs.readFileSync(targetPath, "utf8"));
  } catch (err) {
    console.error("DOSSIER: LAUNCH.json is not valid JSON: " + err.message);
    process.exit(1);
  }
  if (!record.mint || record.mint.indexOf("BELUM DIISI") !== -1) {
    console.error("DOSSIER: LAUNCH.json still holds placeholders — fill mint + create_signature after the mint.");
    process.exit(1);
  }
  if (!record.create_signature || record.create_signature.indexOf("BELUM DIISI") !== -1) {
    console.error("DOSSIER: LAUNCH.json still holds placeholders — fill mint + create_signature after the mint.");
    process.exit(1);
  }
  console.log("DOSSIER: LAUNCH.json copied for mint " + record.mint);
}

main();
