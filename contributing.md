# Contributing

Thanks for considering a contribution — even a small tool benefits from fresh eyes.

## Getting set up

```bash
git clone https://github.com/manishbollikonda-318/QR-Generator.git
cd QR-Generator
pip install -r requirements-dev.txt
```

## Making a change

1. Fork the repo and create a branch off `main`:
   ```bash
   git checkout -b feature/short-description
   ```
2. Make your change. Keep functions small and add a docstring if behavior isn't obvious from the name.
3. Add or update tests in `test_main.py` for anything you change in `main.py`. PRs that change behavior without a matching test won't be merged.
4. Run the full test suite locally before opening a PR:
   ```bash
   pytest test_main.py -v
   ```
5. Update `README.md` if you added or changed a CLI flag.

## Commit messages

Keep them short and specific — `Fix border validation off-by-one` is more useful than `Update main.py`.

## Opening a pull request

- Describe *what* changed and *why*, not just what files were touched.
- Link any related issue.
- Make sure CI is green before requesting review.

## Reporting bugs / requesting features

Use the issue templates under `.github/ISSUE_TEMPLATE/` — they ask for the minimum info needed to act on a report (repro steps, expected vs. actual behavior, environment).

## Code style

- Standard library `argparse` patterns already used in `main.py` — follow the existing structure rather than introducing a new CLI framework.
- Type hints on function signatures where practical.
- No new runtime dependencies without discussion first — this tool is intentionally lightweight.
