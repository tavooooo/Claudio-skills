---
name: recording-app-demos
description: Use when the user wants a video, screen recording, demo clip, walkthrough, or reel/TikTok/Shorts footage of a web app or web page — especially in a headless container with no display, when Playwright browsers are preinstalled, or when the deliverable must be a phone-ready vertical MP4.
---

# Recording App Demos

## Overview

Record a scripted browser walkthrough as a social-ready MP4 (H.264, 1080x1920, 9:16) using Playwright's `recordVideo` + ffmpeg. No display/GUI needed. Works in Claude remote containers.

## The Two Rules That Decide Quality

**1. The CSS viewport must be phone-sized** (below the app's mobile breakpoint, usually <768px). Setting `viewport: 1080x1920` renders the DESKTOP layout — tiny text, huge margins — technically meets the spec, visually wrong for a phone demo.

**2. Playwright NEVER upscales video** — a `recordVideo.size` larger than the viewport letterboxes the capture into the top-left corner of a gray canvas. Record at native viewport size; upscale in ffmpeg.

```
viewport: 540x960 (9:16, still mobile layout) + recordVideo size: 540x960
→ then ffmpeg -vf scale=1080:1920:flags=lanczos
```

## Environment Recipe (Claude remote containers)

| Need | Solution |
|---|---|
| Playwright module | Global install exists: `require('/opt/node22/lib/node_modules/playwright')` — or `npm i playwright-core` locally |
| Chromium | Preinstalled at `/opt/pw-browsers/chromium-*/chrome-linux/chrome`. NEVER run `playwright install` (blocked by env; wastes minutes failing) |
| ffmpeg with H.264 | `command -v ffmpeg || (apt-get update -qq && apt-get install -y -qq ffmpeg)`. Playwright's bundled ffmpeg is VP8-only (no MP4); npm `ffmpeg-static` postinstall is blocked by the proxy — apt is the only working path, and it fails without `update` first |
| The app itself | Local page → `file://` URL; dev app → start it (`npm run dev`) and wait for the port; prod → public URL |

## Working Example

Adapt [record-demo.example.js](record-demo.example.js) (tested in this environment). Key structure:

1. `chromium.launch({ args: ['--no-sandbox'] })` (+ `executablePath` if using playwright-core)
2. `newContext` with the viewport/recordVideo rules above
3. Scripted walkthrough: `goto` → `waitForTimeout(800)` to settle → actions
4. `await ctx.close()` — REQUIRED to flush the .webm before reading `page.video().path()`
5. Convert + upscale: `ffmpeg -y -i in.webm -vf scale=1080:1920:flags=lanczos -c:v libx264 -preset fast -crf 20 -pix_fmt yuv420p -r 30 -movflags +faststart out.mp4` (`yuv420p` is what makes it playable on phones/Instagram)

## Walkthrough Scripting

- Scroll in small smooth steps: `window.scrollBy({top: 600, behavior: 'smooth'})` + ~900ms waits. One giant scroll reads as a glitch on video.
- Interactions: `page.click()` / `page.fill()` with 500–1000ms pauses after each, so viewers can register what happened.
- Target 20–40s total; trim/speed-ramp later in the editor (CapCut), not in the script.
- Real webm duration ≈ sum of your waits; pauses are where the editor adds captions.

## Verify Before Delivering

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,duration -of csv=p=0 out.mp4
ffmpeg -y -v error -i out.mp4 -ss 2 -frames:v 1 frame.png   # then LOOK at it
```

`h264,1080,1920` proves the spec; the extracted frame proves it *looks like a phone screen* (mobile layout, readable text). Both checks, always.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Viewport = final resolution → desktop layout | Phone-sized viewport; upscale in ffmpeg |
| `recordVideo.size` > viewport → capture stuck in top-left corner of gray canvas | Playwright never upscales: `size` = viewport, scale up in ffmpeg |
| Reading `video().path()` before closing context | `await ctx.close()` first — the file isn't flushed until then |
| Delivering the .webm | iPhones/CapCut choke on VP8 — always convert to H.264 MP4 |
| `playwright install` / `ffmpeg-static` downloads | Both blocked here — use preinstalled Chromium + apt ffmpeg |
| Claiming done from ffprobe alone | Extract a frame and look: correct specs ≠ correct rendering |
