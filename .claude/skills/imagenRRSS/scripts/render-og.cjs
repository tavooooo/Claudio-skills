#!/usr/bin/env node
/*
 * render-og.cjs — render a share-image layout through the REAL next/og engine (satori +
 * resvg), so you verify the background actually decodes and text metrics are right — which
 * a sharp overlay cannot tell you. Run from the Next.js repo (so `next/og` and `sharp` resolve).
 *
 *   node render-og.cjs <spec.json> [out.png]      # default out: /tmp/rrss_og.png
 *
 * spec.json:
 * {
 *   "bg": "public/story-podium-bg-2.jpg",   // read off disk, inlined as a data-URI (the robust path)
 *   "canvas": [1080, 1920],
 *   "bgSize": [1080, 1934], "bgTop": -7,     // how the bg is drawn (cover + vertical offset)
 *   "texts": [
 *     { "box": [left, top, w, h], "text": "Russell", "size": 44, "color": "#fff", "weight": 900 },
 *     { "box": [l,t,w,h], "number": "24", "unit": "pts", "size": 66, "color": "#facc15" }  // number centered, unit at left:100%
 *   ]
 * }
 * All box coords are in CANVAS space (already scaled). Each item is centered in its box.
 */
const fs = require('fs')
const path = require('path')
const [, , specPath, outPath] = process.argv
if (!specPath || specPath === '--help') { console.log(fs.readFileSync(__filename, 'utf8').split('*/')[0].replace('/*', '')); process.exit(0) }

const { ImageResponse } = require(require.resolve('next/og', { paths: [process.cwd()] }))
const sharp = require(require.resolve('sharp', { paths: [process.cwd()] }))
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'))
const [CW, CH] = spec.canvas
const mime = spec.bg.endsWith('.png') ? 'image/png' : 'image/jpeg'
const bg = `data:${mime};base64,${fs.readFileSync(spec.bg).toString('base64')}`
const [bgW, bgH] = spec.bgSize || [CW, CH]

const kids = [{ type: 'img', props: { src: bg, width: bgW, height: bgH, style: { position: 'absolute', top: spec.bgTop || 0, left: 0 } } }]
for (const el of spec.texts) {
  const [left, top, width, height] = el.box
  let child
  if (el.number != null) {
    child = { type: 'div', props: { style: { position: 'relative', display: 'flex', alignItems: 'center' }, children: [
      { type: 'span', props: { style: { fontSize: el.size, fontWeight: el.weight || 900, color: el.color }, children: String(el.number) } },
      el.unit ? { type: 'span', props: { style: { position: 'absolute', left: '100%', bottom: Math.round(el.size * 0.12), marginLeft: 6, fontSize: Math.round(el.size * 0.36), fontWeight: 800, color: el.color, whiteSpace: 'nowrap' }, children: el.unit } } : null,
    ].filter(Boolean) } }
  } else {
    child = { type: 'span', props: { style: { fontSize: el.size, fontWeight: el.weight || 900, color: el.color, whiteSpace: 'nowrap' }, children: el.text } }
  }
  kids.push({ type: 'div', props: { style: { position: 'absolute', left, top, width, height, display: 'flex', alignItems: 'center', justifyContent: 'center' }, children: child } })
}

const img = new ImageResponse({ type: 'div', props: { style: { width: '100%', height: '100%', display: 'flex', backgroundColor: spec.bgColor || '#04140c', fontFamily: 'sans-serif' }, children: kids } }, { width: CW, height: CH })
img.arrayBuffer()
  .then((ab) => sharp(Buffer.from(ab)).png().toFile(outPath || '/tmp/rrss_og.png'))
  .then(() => console.log('→', outPath || '/tmp/rrss_og.png'))
  .catch((e) => { console.error('ERR', e.message); process.exit(1) })
