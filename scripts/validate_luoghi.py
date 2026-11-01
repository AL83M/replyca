#!/usr/bin/env python3
"""Controllo non distruttivo di luoghi.json, senza dipendenze esterne."""

import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "luoghi.json"
SKETCHFAB_ID = re.compile(r"^[0-9a-fA-F]{32}$")


def main() -> int:
    errors = []
    warnings = []

    try:
        records = json.loads(PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"ERRORE: impossibile leggere {PATH}: {exc}")
        return 1

    if not isinstance(records, list):
        print("ERRORE: luoghi.json deve contenere un array JSON.")
        return 1

    seen = set()
    for index, record in enumerate(records, 1):
        label = f"luogo #{index}"
        if not isinstance(record, dict):
            errors.append(f"{label}: atteso oggetto JSON")
            continue

        name = record.get("nome")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{label}: nome mancante o vuoto")
        else:
            label = f"{label} ({name})"

        for key, lo, hi in (("lat", -90, 90), ("lon", -180, 180)):
            value = record.get(key)
            if (isinstance(value, bool) or not isinstance(value, (int, float))
                    or not math.isfinite(value) or not lo <= value <= hi):
                errors.append(f"{label}: {key} deve essere un numero tra {lo} e {hi}")

        key = (record.get("nome"), record.get("lat"), record.get("lon"))
        if all(isinstance(x, (str, int, float)) for x in key):
            if key in seen:
                warnings.append(f"{label}: possibile record duplicato")
            seen.add(key)

        platform = record.get("piattaforma")
        model = record.get("modello")
        if platform == "sketchfab" and not (
            isinstance(model, str) and SKETCHFAB_ID.fullmatch(model)
        ):
            errors.append(f"{label}: modello Sketchfab deve essere un ID di 32 caratteri esadecimali")
        elif platform == "luma" and not isinstance(model, str):
            errors.append(f"{label}: modello Luma deve essere una stringa")

        if record.get("tipo") == "panorama360" and not record.get("foto360"):
            errors.append(f"{label}: tipo panorama360 richiede foto360")
        if record.get("foto360") and record.get("tipo") != "panorama360":
            warnings.append(f"{label}: foto360 presente ma il viewer userà la modalità 3D")

        for media_field in ("foto", "foto360"):
            media = record.get(media_field)
            if not isinstance(media, str) or not media.strip():
                continue
            if "://" not in media and not media.startswith(("data:", "/")):
                if not (ROOT / media).is_file():
                    warnings.append(f"{label}: {media_field} relativo non trovato: {media}")

    print(f"Controllati {len(records)} luoghi in {PATH.name}")
    for warning in warnings:
        print(f"AVVISO: {warning}")
    for error in errors:
        print(f"ERRORE: {error}")
    print(f"Risultato: {len(errors)} errori, {len(warnings)} avvisi")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
