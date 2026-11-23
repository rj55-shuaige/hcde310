# Member B — Technical & Data (draft workspace)

**You own:** Sections 4, 5, 6, Code criteria in 8, Section 9, `.github/copilot-instructions.md`, `.gitignore`.

## Section 4 — Data sources

- [ ] Call Open-Meteo with verified resort coordinates; paste trimmed **real** response + observation.
- [ ] Call official NRCS AWDB SNOTEL API with actual station IDs and request parameters; paste trimmed **real** response + observation.
- [ ] Record missing values, station elevation, distance to resort and observation time.
- [ ] Clarify authentication/usage limits from official docs.

## Section 5 — Data model

[Confirm IDs, units, JSON persistence and relationships in `../p2.md`.]

## Section 6 — Tech plan

[Confirm routes, inputs, error states and files. No Flask implementation is required for P2.]

## Section 8 — Code criteria

[Check Many Lenses can be implemented with actual fields available from the APIs.]

## Section 9 — Priorities and risks

[Check station coverage and failure handling early.]
