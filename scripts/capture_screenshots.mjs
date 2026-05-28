import { chromium } from "playwright";

const baseUrl = process.env.ARTIFACT_URL || "http://127.0.0.1:6119";

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1440, height: 1180 } });
await page.goto(baseUrl, { waitUntil: "networkidle" });

await page.locator("#portfolioView").screenshot({ path: "docs/images/opportunity-portfolio.png" });

await page.getByRole("button", { name: "PRD" }).click();
await page.locator("#prdView").screenshot({ path: "docs/images/prd-builder.png" });

await page.getByRole("button", { name: "Launch" }).click();
await page.locator("#launchView").screenshot({ path: "docs/images/launch-readiness.png" });

await page.screenshot({ path: "docs/images/dashboard.png", fullPage: true });

await browser.close();
console.log("Captured portfolio artifact screenshots.");
