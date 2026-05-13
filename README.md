# project_RPS

A DOS-style Rock Paper Scissors game built in Python.

---

## Changelog

### v3.0
- Introduced progressive cheating system:
  - 25% chance (early rounds)
  - 50%, 75%, up to 100% in later rounds

- Added display for:
  - Normal state
  - Cheating status

- Minor code restructuring for feature expansion
- Added comments to `game_start.bat`

---

### v2.0
- General code cleanup

- Improved input validation:
  - No try/except required
  - Custom validation logic implemented

- Introduced `.bat` file for CMD execution:
  - Screen stays static (no scrolling)
  - Screen cleared before redraw (`os.system("clear/cls")`)

- Implemented input overwrite:
  - Invalid input is removed instantly
  - Re-entry without adding new lines (`sys.stdout.write + flush`)

---

### v1.0
- First working prototype

- Basic Rock Paper Scissors logic implemented
- Placeholder ASCII art for game states

- Initial modular structure:
  - Code separated into `game_modules`
  - Included `__init__.py`
