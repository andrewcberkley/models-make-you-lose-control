# Changelog

This file records what changed in each update, newest first. I'm writing the chapters as I go, so each entry matches a new chapter (or, for the first entry, the setup). The format loosely follows [Keep a Changelog](https://keepachangelog.com), and the version goes up by one minor version per chapter, reaching 1.0.0 once every chapter is written.

## 0.1.0 (Setup and getting started)

First release, with the README, the setup instructions, the getting-started notebook and the intros to the chapter text and the solutions.

### Added

- `.gitattributes`, keeps line endings consistent across operating systems
- `.github/ISSUE_TEMPLATE/config.yml`, issue template settings
- `.github/ISSUE_TEMPLATE/found-a-mistake.md`, an issue template for reporting mistakes
- `.github/ISSUE_TEMPLATE/suggestion.md`, an issue template for suggestions
- `.github/workflows/checks.yml`, automatic checks that run the solution notebooks and tests on every push
- `.gitignore`, keeps the virtual environment, caches and generated output out of git
- `CITATION.cff`, citation details, which power GitHub's "Cite this repository" button
- `CONTRIBUTING.md`, how to report mistakes, suggest ideas and send fixes
- `LICENSE`, the MIT licence for the code
- `LICENSE-TEXT.md`, the CC BY-NC 4.0 licence for the written material
- `README.md`, the front page, with setup instructions and the chapters table
- `docs/CHAPTERS.md`, the chapter text, starting with the intro
- `labkit/__init__.py`, the reference toolkit package
- `labkit/checks.py`, the friendly checks the notebooks use to tell you whether you got it
- `notebooks/ch00_getting_started.ipynb`, the getting-started notebook, which shows how the notebooks and checks work
- `requirements.txt`, the Python packages the notebooks need
- `solutions/SOLUTIONS.md`, the solutions to the exercises, starting with the intro
- `solutions/ch00_getting_started_solution.ipynb`, the filled-in copy of the getting-started notebook
- `CHANGELOG.md`, this changelog
