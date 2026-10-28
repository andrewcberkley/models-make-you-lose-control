# Models Make You Lose Control

[![Checks](https://github.com/andrewcberkley/models-make-you-lose-control/actions/workflows/checks.yml/badge.svg)](https://github.com/andrewcberkley/models-make-you-lose-control/actions/workflows/checks.yml) [![Code license: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE) [![Text license: CC BY-NC 4.0](https://img.shields.io/badge/text-CC%20BY--NC%204.0-lightgrey.svg)](LICENSE-TEXT.md)

By Andrew Berkley ([@andrewcberkley](https://github.com/andrewcberkley))

*A hands-on practice lab for loss-of-control evaluation. Music make you lose control, and models might too, so this lab is about noticing when they do.* (With apologies to Missy Elliott. The other names I considered were "Get Ur Evals On" and "Work It: Flip the Monitor and Reverse It.")

## What this is

This is a short, hands-on guide to evaluating AI systems for loss-of-control risk (i.e., the measuring, investigating and code reading you'd do if you were embedded with a lab), written as a series of chapters with companion Jupyter notebooks. Each chapter's text covers the ideas, the readings and a set of self-checks, and its notebook follows the same pattern every time, starting with a realistic situation and an explanation of the idea in plain words, then walking through a worked example before you write small pieces of code yourself, each with a check that tells you right away whether you got it. Every notebook ends with a **Check your understanding** section, where you explain what you found in your own words.

The chapter text lives in `docs/CHAPTERS.md` and the companion notebooks live in `notebooks/`. The exercises are in `exercises/`, and a filled-in copy of every notebook is in `solutions/`, along with the solutions to the exercises (`solutions/SOLUTIONS.md`).

**I'm writing these chapters as I go.** So far Chapter 1 is ready, and since building each chapter takes time, I'll add the next one (i.e., Chapter 2) once it's ready.

Everything here is synthetic, so every address, key, transcript and number is made up and nothing comes from any real organization's systems. The labs you'll work through are fictional too, and I named each one after a Missy Elliott track or something else from that era, with a note in each chapter explaining why.

## Why I made this, and how I approached it

I already work in this space, and most of what I know about loss-of-control evaluation (e.g., testing agents before release, working through red-team results, weighing safety arguments and the statistics that hold them up) I learned by doing it, often through trial and error. Organizations such as METR, Transluce, Redwood Research and the UK AI Security Institute publish a lot of great work, but it's spread across papers, blog posts and codebases, which makes it hard to know where to start or how to practice.

In a previous life I was a lecturer (shout out to the Princeton in Asia fellowship), which meant a lot of time in front of a classroom planning lessons, explaining tricky ideas in plain words and finding out the hard way which explanations actually landed, and I've never quite stopped teaching. I've also been a DJ, turntablist and mash-up artist for over twenty years (i.e., as a hobby and a creative outlet), which is how a lab about AI oversight ended up named after a Missy Elliott track, with a cast of fictional companies named like a throwback setlist.

Most of my day-to-day work is confidential, so I can't share the specifics, but I can share the approach (i.e., the habits and methods that have held up for me), rebuilt here on synthetic data so anyone can practice them. I'm doing this for the public good, because the more people who can do this work carefully, the better.

The approach comes down to a handful of habits.

- **Learn by doing, on data you can't hurt.** Every idea comes with a synthetic dataset or a small simulation where you already know the right answer, so you can find out whether your method actually works.
- **Put statistics first.** Most evaluation claims are rates drawn from small samples near 0% or 100%, which is exactly where evaluations tend to overstate what they show, so honest error bars, base rates and clustering come up in almost every chapter.
- **Treat the model as a possible adversary.** Loss of control differs from accidents and misuse because the system itself might be working around oversight, so threat models, monitors and control protocols are all practiced from that angle.
- **Explain it in your own words.** Each notebook ends with a short "check your understanding" write-up and each capstone exercise ends with a one-page write-up, because the real test of understanding is reaching a defensible conclusion and being able to say it plainly.
- **Separate what you observed from what you inferred.** Claims ledgers, bottom-line-first write-ups and stated confidence levels show up throughout the chapters for exactly this reason.
- **Read the primary sources.** Each chapter points to the papers it's built on, and the chapters are meant as a way in rather than a replacement for them.
- **Make something public.** The final chapter builds toward a short public write-up, since explaining your results to a stranger is the best test of whether you really understand them.

If you're curious about the space (e.g., you're thinking about moving into it, or you just want to understand what evaluators actually do), I hope this saves you some time.

## Set up (once, in Windows PowerShell)

You'll need Python 3.12 or newer. If you'd rather not install anything, every notebook also has an **Open in Colab** badge at the top, which opens it in Google Colab and fetches the rest of the lab for you.

Some computers block the `activate` script, which is a normal security setting, so these commands call the environment's own Python directly and you won't need to activate anything or change any settings. On macOS or Linux, use `python3 -m venv .venv` and `.venv/bin/python` in place of `.venv\Scripts\python`.

1. Clone or download this repository into a folder of your choice.
2. In PowerShell, run these commands one at a time.

```
cd path\to\this\folder
python3 -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m notebook
```

3. A browser tab will open showing the lab folder, where you can open `notebooks` and then `ch00_getting_started.ipynb`.
4. Click the first cell and press **Shift+Enter**, and once it prints `Ready.` you can follow the notebook from there.

To stop Jupyter, close the browser tab and then press **Ctrl+C** in PowerShell. Next time you'll only need these two commands.

```
cd path\to\this\folder
.venv\Scripts\python -m notebook
```

**Prefer VS Code?** Open the lab folder in VS Code, install the Python and Jupyter extensions if it asks, and open a notebook. Then click **Select Kernel** in the top right, choose **Python Environments** and pick the one in `.venv`.

## Working through a chapter

1. Read the chapter in `docs/CHAPTERS.md`, then open its companion notebook in `notebooks/` and run the cells from top to bottom.
2. Read the situation and the idea before you touch any code.
3. Run the worked example and read what it prints, since the text underneath tells you what to notice.
4. Work through each **Your turn** step by filling in the code, running the cell and then running the check under it (and only open a hint if you're stuck).
5. Write your **Check your understanding** answer in your own words before you open the model answer.
6. Compare with the matching notebook in `solutions/` only after you've had a proper go.

## Chapters and exercises

Go at whatever pace suits you. Most chapters have a companion notebook with the same number.

| Chapter | Notebook or exercise | The question it answers |
| --- | --- | --- |
| 0 | Getting-started notebook | How do these notebooks work? |
| 1 | Chapter 1 notebook. How sure can you be when nothing went wrong? | What do zero failures in 300 tests actually rule out? |
| 1 | Chapter 1 exercise. Threat model | What could go wrong with a lab's internal coding agent? |

## What's in the folder

- `docs/` holds the chapters themselves (`docs/CHAPTERS.md`), with each chapter's ideas, readings and self-checks.
- `notebooks/` holds the companion notebooks, and it's where you'll do most of your hands-on work.
- `solutions/` holds a filled-in copy of every notebook and the solutions to the exercises (`solutions/SOLUTIONS.md`).
- `exercises/` holds the end-of-chapter exercises, including the two capstone exercises.
- `labkit/` is the reference code the notebooks build on, and while you don't need to edit it, reading it is good practice.
- `CHANGELOG.md` records what changed in each update, so you can see at a glance what's new since you last looked.

## If something goes wrong

- **`No module named ...`.** The install step didn't finish, so run the `pip install` line again.
- **`NameError` in a cell.** An earlier cell hasn't been run yet, so either use the menu (i.e., Kernel, then Restart Kernel and Run All Cells) or run the cells above it.
- **The setup cell doesn't print `Ready.`.** Make sure you opened the notebook from inside the lab folder.
- **`python -m notebook` doesn't start.** Try `.venv\Scripts\jupyter-notebook` instead.
- **VS Code uses the wrong Python.** Select the `.venv` kernel as described above.
- **A check says Not yet and you can't see why.** Open the hint, compare your code with the solutions notebook, or paste the cell and its message into Copilot and ask what's wrong.

## Ground rules

Use synthetic setups, public data and personal accounts only.

## Found a mistake or have an idea?

Please open an issue (there are templates for mistakes and suggestions), and see `CONTRIBUTING.md` if you'd like to send a fix. Since I'm still writing later chapters, small fixes are the easiest for me to take on right away.

## License

The code (i.e., the Python files, the code cells in the notebooks and the synthetic data) is under the MIT license in `LICENSE`, so you can reuse it freely. The written material (i.e., the chapters, the notebook prose, the exercises and the solutions) is under CC BY-NC 4.0, as described in `LICENSE-TEXT.md`, which means you're welcome to share and adapt it with credit, but not to use it commercially without asking me first. If you use or adapt this material, GitHub's "Cite this repository" button (from `CITATION.cff`) gives you a ready-made citation.

## Disclaimer

This is a personal project, so the views and approaches here are my own and don't represent any employer or other organization, and nothing here is official guidance. The fictional companies are an affectionate tribute, and this project isn't affiliated with or endorsed by Missy Elliott, her labels, or any of the organizations whose public research I point to. This guide grew out of my own experience, and I used AI tools as a thought partner along the way (e.g., to pressure-test my reasoning, debug code and help with drafting and editing), so the ideas, choices and any mistakes are mine.
