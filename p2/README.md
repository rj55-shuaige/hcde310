# Snow Compare — HCDE 310 starter

This is a **runnable prototype + P2 proposal scaffold**, not a finished or verified submission. It uses live Open-Meteo weather when internet access is available. The included resort records are **provisional demo coordinates**, **not** a real OpenSkiData import. You must finish second-source integration and provide real evidence.

## How to run from a fresh clone (VS Code terminal)

```bash
python3 -m venv .venv
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env
# Windows PowerShell: Copy-Item .env.example .env
python app.py
```

Then open **http://127.0.0.1:5000** in your browser. Select two different resorts, compare conditions, save favorites, and refresh the homepage to verify persistence.

## Gather genuine API data for the proposal

```bash
python collect_evidence.py
```

Requires an internet connection. Paste a trimmed **actual** response into `P2/p2.md` Section 4 and write your own observation. **You also must independently download/inspect a real OpenSkiData record** and replace the provisional `data/resorts.json` values.

## File structure

- `P2/p2.md`: 11-section English proposal draft (TODOs remain)
- `P2/mockups/`: initial layout drafts, **not** substitutes for student sketches
- `P2/ai_use.md`: AI usage log starter
- `.github/copilot-instructions.md`: context draft; check class template
- `app.py`: Flask routes
- `weather.py`: Open-Meteo request
- `resorts.py`: resort data reading
- `summary.py`: weather comparisons in Python
- `data/favorites.json`: saved favorites
- `data/resorts.json`: provisional demo catalogue

## Accessibility checks

The code provides form labels, clear headings, accessible table headers, visible keyboard focus, and text alerts. Test with keyboard and real users.

## Before submission

Read all **TODO** items in `P2/p2.md`. Replace prototype data and wireframes, validate real responses for two sources, and review `.github/copilot-instructions.md` with your Stage 4 class template. Ensure `.env` does not appear in `git status`. Commit and push, then submit a GitHub commit link on Canvas.
