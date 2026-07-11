---
name: imagenRRSS
description: Use when adding or fixing a downloadable social-media share image (a story/podium/ranking card composed over a background template with next/og — "imagen para compartir", "story", "podio", "RRSS", Instagram/WhatsApp 9:16) where text must land inside printed boxes on the artwork.
---

# imagenRRSS — Share images (RRSS) over a background template

## Overview

Generate a vertical share image by absolutely positioning text so it lands **inside boxes
printed on a background artwork**, rendered server-side with `next/og`. The whole job is:
measure the boxes accurately, register their coordinates, center text in them, and verify
with a **real next/og render** — not just an image overlay.

Core principle: **the artwork is the source of truth for positions.** Measure it; don't guess.

## When to use

- Adding a new background/template for a downloadable story/podium/ranking card.
- Fixing text that sits off-center, overflows a box, or a background that renders blank.
- Any `next/og` (`ImageResponse`) image composed over a raster template.

## Process

1. **Add the background** to the public assets as a **baseline JPEG** (photographic art with
   no transparency → ~10× smaller than PNG). **Never progressive:**
   `sharp(src).jpeg({ quality: 88, progressive: false })`. `mozjpeg:true` emits progressive — avoid.
2. **Measure the boxes** — `scripts/measure.cjs` (sharp):
   - `grid <img> [y0 y1]` → overlays a coordinate grid; read approximate box extents.
   - `rows <img> x0 x1 y0 y1` and `cols <img> x0 x1 y0 y1` → the box outlines are BRIGHTER
     than the fill, so bright rows/cols give the **top/bottom** and **left/right** edges.
   - `overlay <img> '<json-boxes>'` → draw your measured boxes back on the art to confirm.
   Measure the top AND bottom line of each box so text can be vertically centered inside it.
3. **Register** the template coordinates in **native px** of the PNG. Scale to the canvas once:
   `scale = CANVAS_W/native; S(box) = {left:l*scale, top:t*scale+offsetY, w:w*scale, h:h*scale}`
   where `offsetY = round((CANVAS_H - round(nativeH*scale))/2)`. Center text with flex
   (`alignItems/justifyContent: center`) inside `S(box)`.
4. **Bundle the asset into the function** so it can be read off disk (public assets are
   CDN-only otherwise): add it to `outputFileTracingIncludes` for the image route.
5. **Verify with a real next/og render** — `scripts/render-og.cjs`. Overlays from sharp only
   prove geometry; only next/og proves the background decodes and text metrics are right.

## Gotchas (each cost a round-trip — don't repeat)

| Symptom | Cause | Fix |
|---|---|---|
| Background renders **blank/black** | `<img src>` fetched over HTTP raced a cold CDN for a freshly-deployed asset | Read the file from disk and inline as a **data-URI** (`data:image/jpeg;base64,…`); fallback to fetch. Requires the file be traced into the function (step 4). |
| Background blank, decodes locally | **Progressive** JPEG | Re-encode **baseline** (`progressive:false`). Check with `sharp(f).metadata().isProgressive`. |
| Text sits low / off-center | Box coords wrong (guessed, not measured) | Detect the real top+bottom edges (step 2) and center inside them. |
| Number not centered when a unit (`pts`) rides beside it | Whole `[number][unit]` group is centered | Wrap the number in a `position:relative` centered div; put the unit `position:absolute; left:'100%'` so only the NUMBER centers. |
| Long name overflows box | No truncation (next/og has no text-overflow) | Shrink font by length, then hard-truncate with `…` using a char budget = `boxWidth / (fontSize*0.6)`. |
| Podium shows a name twice on a tie | Sliced by the `position` field | Slice the sorted array by INDEX (`.slice(0,3)`, `.slice(3,8)`), never filter on `position`. |

## Verifying with next/og locally

`next/og` isn't ESM-resolvable by bare specifier in a script; require the file:
`const { ImageResponse } = require('<repo>/node_modules/next/og.js')` (or `require('next/og')`
from the repo root). Build the element tree as plain `{type, props}` objects, inline the
background as a data-URI, `await img.arrayBuffer()`, write the PNG, and eyeball it. Run
`node scripts/render-og.cjs --help` for the spec format.

## Quick reference

- Canvas: 1080×1920 (9:16). Template ratio a hair taller → cover + vertical `offsetY`.
- Podium: 3 on the podium + 5 in the list (max 8).
- Coordinates live in **native PNG px**; scale to canvas in one place.
- Points font sized to fill the box: `round(boxHeight * 0.72)` (2 digits), `*0.54` (3+).
