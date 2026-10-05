#!/usr/bin/env python3
"""Genera index.html (PWA instalable) a partir de dashboard.html.

dashboard.html es el "cuerpo" que también se publica como artifact de Claude
(sin <html>/<head>/<body>, porque el artifact los agrega). Para servirlo como
web propia (Vercel) e instalarlo en el teléfono como Kiwiano, necesita un
documento completo con <head>: manifest, apple-touch-icon y metas de PWA.

Este script envuelve ese cuerpo con el <head> correcto. El loop diario lo corre
después de copiar dashboard.html para mantener index.html sincronizado.

Uso:  python3 build-pwa.py
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "dashboard.html")
OUT = os.path.join(HERE, "index.html")

HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Torre de Control</title>
<meta name="description" content="Panel de control del portfolio de Gustavo">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" type="image/png" href="icon-512.png">
<meta name="theme-color" content="#040807">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Torre">
<style>*{box-sizing:border-box}html,body{margin:0;padding:0;background:#040807}</style>
</head>
<body>
"""

FOOT = "\n</body>\n</html>\n"


def main() -> None:
    with open(SRC, encoding="utf-8") as f:
        body = f.read()
    # el cuerpo del artifact empieza con <title>...</title>: sobra en un doc real
    body = re.sub(r"^\s*<title>.*?</title>\s*", "", body, count=1, flags=re.S)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(HEAD + body + FOOT)
    print("index.html generado (" + str(os.path.getsize(OUT)) + " bytes)")


if __name__ == "__main__":
    main()
