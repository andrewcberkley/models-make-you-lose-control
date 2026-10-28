# Contributing

Thanks for wanting to help. I'm writing these chapters as I go, so the most useful thing you can do is tell me when something's wrong or unclear (e.g., a typo, a broken cell, a check that fails when your answer looks right, or an explanation that didn't land).

## Reporting a problem or suggesting an idea

Please open an issue and pick the template that fits (i.e., "Found a mistake" or "Suggestion"). The templates ask for the chapter, the notebook cell or file, and what you expected to happen, which makes it much quicker for me to fix.

## Pull requests

Small fixes (e.g., typos, broken links or a clearer sentence) are very welcome as pull requests. For anything bigger (e.g., a new exercise, a change to how a chapter is structured or a change to the toolkit), please open an issue first so we can talk it through, because I'm still writing later chapters and the earlier ones build toward them.

If your change touches code, please run the checks before you open the pull request (the same ones GitHub runs automatically).

```
python -m pytest tests          # with LAB_SOLUTIONS=1 set, to run against the reference fix
python make_data.py             # the data files shouldn't change
```

## Ground rules

- Only use synthetic setups and public data, and never add anything confidential (e.g., real transcripts, prompts or internal documents from any organization).
- Keep the tone friendly and plain, and explain ideas so that someone new to the field can follow them.
- By contributing, you agree that your contributions are licensed under the same terms as the rest of the repository (i.e., MIT for code and CC BY-NC 4.0 for written material, as described in `LICENSE` and `LICENSE-TEXT.md`).
