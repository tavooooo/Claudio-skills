#!/usr/bin/env python3
"""Hook Stop: suma los tokens de la sesión y los anota en docs/metricas/tokens.csv.

Corre automáticamente después de cada respuesta de Claude (ver .claude/settings.json).
La fila de cada sesión es ACUMULATIVA (se reemplaza, no se duplica).
"""
import json
import os
import sys
from datetime import date

def main() -> None:
    try:
        hook = json.load(sys.stdin)
    except Exception:
        return
    transcript = hook.get("transcript_path")
    session = (hook.get("session_id") or "desconocida")[:12]
    if not transcript or not os.path.exists(transcript):
        return

    tokens_in = tokens_out = 0
    with open(transcript, encoding="utf-8") as f:
        for line in f:
            try:
                entry = json.loads(line)
            except Exception:
                continue
            message = entry.get("message")
            if not isinstance(message, dict):
                continue
            usage = message.get("usage")
            if not isinstance(usage, dict):
                continue
            tokens_in += (usage.get("input_tokens") or 0)
            tokens_in += (usage.get("cache_creation_input_tokens") or 0)
            tokens_in += (usage.get("cache_read_input_tokens") or 0)
            tokens_out += (usage.get("output_tokens") or 0)

    if tokens_in == 0 and tokens_out == 0:
        return

    csv_path = os.path.join("docs", "metricas", "tokens.csv")
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    header = "fecha,session,tokens_entrada_acum,tokens_salida_acum"
    rows = []
    if os.path.exists(csv_path):
        with open(csv_path, encoding="utf-8") as f:
            lines = f.read().splitlines()
        rows = [
            r for r in lines[1:]
            if r.strip() and r.split(",")[1] != session
        ]
    rows.append(f"{date.today().isoformat()},{session},{tokens_in},{tokens_out}")
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write(header + "\n" + "\n".join(rows) + "\n")

if __name__ == "__main__":
    main()
