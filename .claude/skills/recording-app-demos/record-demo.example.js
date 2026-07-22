// Records a scripted walkthrough as a 9:16 phone-look video.
// Run: node record-demo.example.js [url]  → prints the .webm path, then convert (see below).
// Requires: playwright OR playwright-core (+ executablePath) — see SKILL.md env recipe.
//
// Convert + upscale to Reels-ready MP4 (Playwright never upscales, ffmpeg does):
//   ffmpeg -y -i vids/<file>.webm -vf scale=1080:1920:flags=lanczos \
//     -c:v libx264 -preset fast -crf 20 -pix_fmt yuv420p -r 30 -movflags +faststart out.mp4

const playwright = require('/opt/node22/lib/node_modules/playwright'); // global install in Claude containers
// const playwright = require('playwright-core');                      // local alternative

const TARGET = process.argv[2] || 'file:///home/user/fitmark/docs/marketing/calendario-contenidos.html';

(async () => {
  const browser = await playwright.chromium.launch({
    args: ['--no-sandbox'],
    // executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', // needed with playwright-core
  });

  const ctx = await browser.newContext({
    // 540x960: 9:16 AND below typical mobile breakpoints (<768px) → phone layout.
    // recordVideo.size MUST equal the viewport — larger sizes letterbox into a gray canvas.
    viewport: { width: 540, height: 960 },
    recordVideo: { dir: 'vids', size: { width: 540, height: 960 } },
  });

  const page = await ctx.newPage();
  await page.goto(TARGET, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1200); // opening hold — room for a caption in the editor

  // --- Walkthrough: edit this section per demo ---
  for (let i = 0; i < 6; i++) {
    await page.evaluate(() => window.scrollBy({ top: 600, behavior: 'smooth' }));
    await page.waitForTimeout(900); // small steps read as intentional, not glitchy
  }
  // Interactions look like: await page.click('text=Rutinas'); await page.waitForTimeout(800);
  // ------------------------------------------------

  await page.waitForTimeout(1000); // closing hold
  await ctx.close();               // REQUIRED: flushes the video file
  console.log('webm:', await page.video().path());
  await browser.close();
})();
