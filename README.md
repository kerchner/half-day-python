# Python in Half a Day 🐍

Slides and notebooks for **"Python in Half a Day"**, an introductory, hands-on Python
workshop offered by [George Washington University Libraries and Academic Innovation](https://library.gwu.edu).

## Contents

### Notebooks from the workshop:
- `notebooks/` — the **student** versions of the workshop notebooks: all of the
  explanatory text, with the code cells left **empty** for you to fill in as we
  go. Open them in [Google Colab](https://colab.research.google.com) or Jupyter.
  - [Part 1 Notebook](https://colab.research.google.com/github/kerchner/half-day-python/tree/main/notebooks/Python_Workshop_Part_1.ipynb) - the Python language: variables,
    lists, dictionaries, loops, conditionals, functions, importing libraries
  - `Python_Workshop_Part_2_*_student.ipynb` — data with `pandas`: loading,
    exploring, subsetting, summarizing, merging, and plotting
- `jupyter notebooks/` — the instructor ("filled out") versions, with all the code
- `data/` — local copies of the datasets used in Part 2 (`surveys.csv`, `species.csv`),
  a subset of the [Portal Project Teaching Database](https://figshare.com/articles/Portal_Project_Teaching_Database/1314459)

### Code for the slides:
- `index.qmd` — the workshop slides ([Quarto](https://quarto.org) / reveal.js)
- `custom.scss` — the slide theme (Python blue & yellow)
- `docs/` — the rendered site, served by GitHub Pages

### Maintenance:
- `scripts/make_student_notebooks.py` — regenerates the student notebooks in
  `notebooks/` from the instructor notebooks in `notebooks_completed/` (keeps
  the markdown, blanks every code cell). Run it after editing the instructor
  notebooks:

  ```sh
  python3 scripts/make_student_notebooks.py
  quarto render
  ```

## Workshop resources

- 📅 GW Libraries workshops & events: <https://library.gwu.edu/events>
- 🐍 Official Python tutorial: <https://docs.python.org/3/tutorial/>
- 🐼 pandas getting-started guide: <https://pandas.pydata.org/docs/getting_started/>
