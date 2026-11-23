import json
from pathlib import Path

RESORT_FILE = Path(__file__).parent / "data" / "resorts.json"


def load_resorts():
    with RESORT_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def find_resort(resorts, resort_id):
    return next((r for r in resorts if r["id"] == resort_id), None)
