# Changelog

This file records what changed in each update, newest first. I'm writing the chapters as I go, so each entry matches a new chapter (or, for the first entry, the setup). The format loosely follows [Keep a Changelog](https://keepachangelog.com), and the version goes up by one minor version per chapter, reaching 1.0.0 once every chapter is written.

## 0.2.0 (Chapter 1. Loss-of-control threat models)

Adds Chapter 1 on loss-of-control threat models, with its notebook (i.e., how sure you can be when nothing went wrong), the threat-model exercise and the statistics toolkit, and switches the text to American spelling throughout.

### Added

- `exercises/README.md`, the index of exercises
- `exercises/ch01_threat_model/scenario.md`, the Chapter 1 exercise scenario
- `exercises/ch01_threat_model/template.md`, the Chapter 1 exercise template
- `labkit/stats.py`, reference statistics code (e.g., Wilson intervals and zero-failure bounds)
- `notebooks/ch01_zero_failures.ipynb`, the companion notebook for Chapter 1
- `solutions/ch01_zero_failures_solution.ipynb`, the filled-in copy of the Chapter 1 notebook

### Changed

- `.github/ISSUE_TEMPLATE/suggestion.md`, switched to American spelling
- `CITATION.cff`, bumped the version to 0.2.0 and added my ORCID iD to the author details
- `CONTRIBUTING.md`, switched to American spelling
- `LICENSE`, switched to American spelling
- `LICENSE-TEXT.md`, switched to American spelling
- `README.md`, added Chapter 1 to the chapters table and updated the note on what's written so far, and switched to American spelling
- `docs/CHAPTERS.md`, added the text of Chapter 1, plus any glossary terms and readings it introduces
- `notebooks/ch00_getting_started.ipynb`, added Chapter 1 to the roadmap, and switched to American spelling
- `solutions/SOLUTIONS.md`, added the model answers for Chapter 1
- `solutions/ch00_getting_started_solution.ipynb`, added Chapter 1 to the roadmap, and switched to American spelling
- `CHANGELOG.md`, added this update's entry

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
- `LICENSE`, the MIT license for the code
- `LICENSE-TEXT.md`, the CC BY-NC 4.0 license for the written material
- `README.md`, the front page, with setup instructions and the chapters table
- `docs/CHAPTERS.md`, the chapter text, starting with the intro
- `labkit/__init__.py`, the reference toolkit package
- `labkit/checks.py`, the friendly checks the notebooks use to tell you whether you got it
- `notebooks/ch00_getting_started.ipynb`, the getting-started notebook, which shows how the notebooks and checks work
- `requirements.txt`, the Python packages the notebooks need
- `solutions/SOLUTIONS.md`, the solutions to the exercises, starting with the intro
- `solutions/ch00_getting_started_solution.ipynb`, the filled-in copy of the getting-started notebook
- `CHANGELOG.md`, this changelog
