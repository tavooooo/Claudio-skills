#!/usr/bin/env node
/*
 * measure.cjs — measure the printed boxes on a background artwork so text can be centered
 * inside them. Run from a repo that has `sharp` installed (e.g. the Next.js app).
 *
 *   node measure.cjs grid    <img> [y0 y1]              # overlay a coordinate grid → /tmp/rrss_grid.png
 *   node measure.cjs rows    <img> x0 x1 y0 y1 [thr]    # bright ROWS → box top/bottom edges
 *   node measure.cjs cols    <img> x0 x1 y0 y1 [thr]    # bright COLS → box left/right edges
 *   node measure.cjs overlay <img> '<json>'            # draw measured boxes back on the art
 *        json = [["label",left,top,width,height,"#hex"], ...]           → /tmp/rrss_overlay.png
 *
 * The box OUTLINES are brighter than both the fill and the surrounding art, so a
 * luminance threshold per row/column reliably locates each edge line.
 */
const sharp = require(require.resolve('sharp', { paths: [process.cwd()] }))
const [, , mode, imgPath, ...rest] = process.argv

if (!mode || !imgPath || mode === '--help') {
  console.log(require('fs').readFileSync(__filename, 'utf8').split('*/')[0].replace('/*', ''))
  process.exit(0)
}

async function raw() {
  const { data, info } = await sharp(imgPath).raw().toBuffer({ resolveWithObject: true })
  const W = info.width, H = info.height, ch = info.channels
  const lum = (x, y) => { const i = (y * W + x) * ch; return data[i] * 0.3 + data[i + 1] * 0.6 + data[i + 2] * 0.1 }
  return { W, H, lum }
}

;(async () => {
  if (mode === 'grid') {
    const meta = await sharp(imgPath).metadata()
    const W = meta.width
    const y0 = rest[0] ? +rest[0] : 0
    const y1 = rest[1] ? +rest[1] : meta.height
    const band = y1 - y0
    let g = ''
    for (let x = 0; x <= W; x += 20) { const M = x % 100 === 0; g += `<line x1="${x}" y1="0" x2="${x}" y2="${band}" stroke="${M ? '#ff0080' : '#ff008055'}" stroke-width="${M ? 1.5 : 0.6}"/>`; if (M) g += `<text x="${x + 2}" y="14" fill="#ff0080" font-size="13" font-family="sans-serif">${x}</text>` }
    for (let y = y0; y <= y1; y += 20) { const M = y % 100 === 0; const yy = y - y0; g += `<line x1="0" y1="${yy}" x2="${W}" y2="${yy}" stroke="${M ? '#00e5ff' : '#00e5ff55'}" stroke-width="${M ? 1.5 : 0.6}"/>`; g += `<text x="2" y="${yy - 2}" fill="#00e5ff" font-size="13" font-family="sans-serif">${y}</text>` }
    const svg = `<svg width="${W}" height="${band}" xmlns="http://www.w3.org/2000/svg">${g}</svg>`
    await sharp(imgPath).extract({ left: 0, top: y0, width: W, height: band }).composite([{ input: Buffer.from(svg), top: 0, left: 0 }]).resize(Math.round(W * 1.6)).png().toFile('/tmp/rrss_grid.png')
    console.log('→ /tmp/rrss_grid.png')
  } else if (mode === 'rows' || mode === 'cols') {
    const { lum } = await raw()
    const [x0, x1, y0, y1] = rest.slice(0, 4).map(Number)
    const thr = rest[4] ? +rest[4] : null
    const outer = mode === 'rows' ? [y0, y1] : [x0, x1]
    const inner = mode === 'rows' ? [x0, x1] : [y0, y1]
    const counts = []
    for (let a = outer[0]; a <= outer[1]; a++) {
      let c = 0
      for (let b = inner[0]; b <= inner[1]; b++) { const L = mode === 'rows' ? lum(b, a) : lum(a, b); if (L > (thr ?? 90)) c++ }
      counts.push([a, c])
    }
    const mx = Math.max(...counts.map((r) => r[1]))
    console.log(`${mode} peaks (max=${mx}${thr ? '' : ', auto-thr 90'}):`)
    for (const [a, c] of counts) if (c >= mx * 0.5) console.log(' ', a, 'count', c)
  } else if (mode === 'overlay') {
    const boxes = JSON.parse(rest[0])
    const meta = await sharp(imgPath).metadata()
    let r = ''
    for (const [l, x, y, w, h, c] of boxes) {
      r += `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="none" stroke="${c || '#ff2d78'}" stroke-width="2.5"/>`
      r += `<line x1="${x + w / 2}" y1="${y}" x2="${x + w / 2}" y2="${y + h}" stroke="${c || '#ff2d78'}" stroke-width="1" stroke-dasharray="4"/>`
      r += `<text x="${x + 4}" y="${y + 16}" fill="${c || '#ff2d78'}" font-size="14" font-family="sans-serif" font-weight="bold">${l}</text>`
    }
    const svg = `<svg width="${meta.width}" height="${meta.height}" xmlns="http://www.w3.org/2000/svg">${r}</svg>`
    await sharp(imgPath).composite([{ input: Buffer.from(svg), top: 0, left: 0 }]).png().toFile('/tmp/rrss_overlay.png')
    console.log('→ /tmp/rrss_overlay.png')
  } else {
    console.error('unknown mode:', mode)
    process.exit(1)
  }
})().catch((e) => { console.error('ERR', e.message); process.exit(1) })
