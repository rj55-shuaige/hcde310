# Class 12 demos

Three small demos from today's class. Open each folder on its own in VS Code.

1. **1-get-post/**: the books app. Search, look at the URL, then follow the comment above `/results` in `app.py` to flip it from GET to POST.
2. **2-pytest/**: the same books app with a test. Run `pytest` (or `python3 -m pytest`) in that folder.
3. **3-agent/**: only a spec. Try the Copilot routine on it: commit first, Plan mode, read the plan against the spec, then say go in Interactive with Permissions on Manual, read the diff, run the checks.

Needs flask, requests and pytest (with .venv on):
python3 -m pip install flask requests pytest
