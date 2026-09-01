# Python Programming: Python `DRAFT`

*GW Libraries & Academic Innovation — Research Guides*

Guide author: **Daniel Kerchner**, Senior Software Developer / Librarian — [Email me](mailto:kerchner@gwu.edu)

Subjects: Datasets and Statistics

---

## Academic Commons Graduate Data Consultants

The Data Consulting Program provides free, one-on-one support to members of the GW community who are working with quantitative data. The data consultants can help develop skills with analyzing data in Python, R, Stata, SAS, SPSS, or building confidence with statistical concepts. Our consultants can assist with everything from foundational statistics to advanced analysis, data visualization, and troubleshooting code.

[Make an appointment with a Data Consultant](https://library.gwu.edu/academic-commons/research-data-assistance)

---

## What is Python?

Python is a free, open-source, general-purpose programming language that has become one of the most widely used languages for data analysis, scientific computing, and machine learning. Python is a popular and powerful tool for researchers in any field working with data: it allows users to clean, manipulate, and analyze data, build statistical and machine-learning models, automate repetitive tasks, collect data from the web, and create publication-quality visualizations. Python is known for its readable syntax, which makes it a good first programming language.

Because Python is a scripted language, researchers can more easily ensure that their analyses are reproducible.

Python itself is maintained by the [Python Software Foundation](https://www.python.org/psf/), and hundreds of thousands of community-developed packages are available through [PyPI](https://pypi.org/) (the Python Package Index) and [conda-forge](https://conda-forge.org/). Packages such as [pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), [matplotlib](https://matplotlib.org/), [SciPy](https://scipy.org/), [statsmodels](https://www.statsmodels.org/), and [scikit-learn](https://scikit-learn.org/) form the core of Python's data-science ecosystem.

There are several apps and environments available for coding in Python. Many researchers work in [Jupyter](https://jupyter.org/) notebooks, which mix narrative text, code, and output in a single document, either locally (JupyterLab) or in the cloud ([Google Colab](https://colab.research.google.com/)). Popular editors include [VS Code](https://code.visualstudio.com/), and [Positron](https://positron.posit.co/), a newer data-science IDE from Posit that is well suited for mixing Python and R workflows.

---

## Downloading / Installing Python

To install Python on your computer, choose **one** of the following:

1. **Anaconda or Miniforge (recommended for data analysis).** Download the [Anaconda Distribution](https://www.anaconda.com/download), which bundles Python with hundreds of data-science packages, JupyterLab, and the Spyder IDE; or install the lighter-weight [Miniforge](https://conda-forge.org/download/), which gives you Python plus the `conda` package manager and lets you install just the packages you need (`conda install pandas matplotlib jupyterlab`).
2. **Python from python.org.** Download the standard installer from [python.org/downloads](https://www.python.org/downloads/). Then install packages with `pip` (for example, `pip install pandas matplotlib jupyterlab`). Windows users should check the box to **Add Python to PATH** during installation.

After installing Python, install an editor or notebook environment:

- [JupyterLab](https://jupyter.org/install) — the browser-based notebook interface (included with Anaconda).
- [VS Code](https://code.visualstudio.com/docs/python/python-tutorial) with the Python and Jupyter extensions — a free, general-purpose editor that supports both scripts and notebooks.
- [Positron](https://positron.posit.co/) — a free, next-generation data-science IDE for Python and R, built on VS Code.
- [Spyder](https://www.spyder-ide.org/) — a free scientific IDE that feels like RStudio or MATLAB (included with Anaconda).
- [PyCharm](https://www.jetbrains.com/pycharm/) — a full-featured professional Python IDE (free Community edition; free Professional licenses for students).

It is recommended that you create a separate **virtual environment** for each project (using `conda create` or `python -m venv`), so that package versions for different projects do not collide. See the [Python packaging guide on virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

You can also use Python in the cloud through your browser, with nothing to install, at [Google Colab](https://colab.research.google.com/) (requires a Google account; the free version has limits on memory, session length, and GPU access).

---

## Finding and Getting Help Using Python at GW

Python is free to install on Windows, Mac, and Linux computers, and Python (including Anaconda) is also available for students, staff, faculty, and affiliates within GW's [Virtual Computer Lab (VCL)](https://it.gwu.edu/virtual-computer-lab-vcl), provided by [GW Information Technology](https://it.gwu.edu). Researchers who need more computing power can request access to [GW High Performance Computing (HPC)](https://it.gwu.edu/hpc), which provides Python and JupyterLab through [Open OnDemand](http://ood.arc.gwu.edu/).

GW Libraries offers [workshops](https://library.gwu.edu/events?format=workshop) to help you get started learning coding, including Python and R. Slides and notebooks from our introductory workshop, *Python in Half a Day*, are available at [kerchner.github.io/half-day-python](https://kerchner.github.io/half-day-python). We also offer the following types of individual consultations:

- [Coding Consultations](https://calendly.com/gwul-coding) with a software developer librarian skilled in Python or R programming.
- [Data Consultations](http://go.gwu.edu/dataconsulting) with graduate students in Academic Commons who are skilled in statistics and statistical analysis using Python, R, SAS, SPSS, STATA, and Excel.

---

## Python for Beginners

[Software Carpentry](https://software-carpentry.org) and [Data Carpentry](https://datacarpentry.org/) online workshop materials provide an excellent way to learn Python in a free, self-paced fashion. Recommended Carpentries materials for beginners to learn Python include the following:

- **[Plotting and Programming in Python](https://swcarpentry.github.io/python-novice-gapminder/)** — This Software Carpentry lesson is an introduction to Python for people with little or no previous programming experience. You will learn Python basics (variables, lists, loops, conditionals, and functions), how to read CSV data with the pandas library, and how to create plots. It uses the Gapminder data on countries' GDP and life expectancy.
- **[Data Analysis and Visualization in Python for Ecologists](https://datacarpentry.org/python-ecology-lesson/)** — In this Data Carpentry workshop, you will learn Python basics, how to read a CSV-formatted data file into a pandas DataFrame, how to index, slice, and subset data, how to combine DataFrames, how to write functions, and how to create data visualizations using plotnine. You do not need to be an ecologist to benefit from this workshop!
- **[Data Analysis and Visualization with Python for Social Scientists](https://datacarpentry.org/python-socialsci/)** — In this Data Carpentry workshop, you will learn Python basics, how to work with data files using pandas, how to process JSON data, how to aggregate and combine data, and how to create data visualizations with matplotlib. You do not need to be a social scientist to benefit from this workshop!

If you prefer learning from an e-book, these free, detailed introductions are excellent:

- **[Python for Data Analysis (3rd edition)](https://wesmckinney.com/book/)** — This book by Wes McKinney, the creator of pandas, is the definitive introduction to data wrangling with Python. You will learn to use Python, NumPy, and pandas to import, clean, transform, aggregate, and visualize data, working in Jupyter notebooks.
- **[Python for Everybody](https://www.py4e.com/)** — Charles Severance's free book, videos, and exercises teach the fundamentals of Python programming with an emphasis on working with data — files, web data, databases, and data visualization. No prior programming experience is assumed.
- **[Automate the Boring Stuff with Python (3rd edition)](https://automatetheboringstuff.com/)** — Al Sweigart's practical, free online book teaches Python by having you automate everyday tasks: renaming files, working with spreadsheets and PDFs, scraping web pages, sending email, and more.
- **[The Python Tutorial](https://docs.python.org/3/tutorial/)** — The official tutorial from python.org. Concise and authoritative; a good reference once you've gotten your feet wet.

---

## Python for Data Analysis: pandas and Polars

Most data analysis in Python happens in a **DataFrame** — a table of rows and named columns, much like a spreadsheet or an R `data.frame`. Two libraries provide DataFrames in Python:

**pandas** is the long-established standard (since 2008). Nearly every tutorial, textbook, and data-science library (matplotlib, seaborn, statsmodels, scikit-learn, GeoPandas) works with pandas DataFrames, so it is the right place to start. pandas reads and writes CSV, Excel, JSON, SQL, Stata, SPSS, SAS, and Parquet; and it handles subsetting, missing data, grouping and aggregation, merging/joining, reshaping (pivoting), time series, and quick plotting.

- **[pandas: Getting started](https://pandas.pydata.org/docs/getting_started/index.html)** — The official introduction, including the "10 minutes to pandas" tour and a set of short "Getting started" tutorials organized by task (selecting subsets, creating plots, combining tables, handling time series, working with text).
- **[pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)** — The comprehensive reference for every part of the library, with worked examples.
- **[pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)** — A two-page reference to the most common pandas operations for data wrangling.
- **[Python for Data Analysis (3rd edition)](https://wesmckinney.com/book/)** — The free online book by pandas creator Wes McKinney (see *Python for Beginners*, above) is the best in-depth guide to pandas.
- **[Data Analysis and Visualization in Python for Ecologists](https://datacarpentry.org/python-ecology-lesson/)** — The Data Carpentry lesson (see above) is a hands-on, pandas-centered introduction with a real dataset.
- **[Effective Pandas: Patterns for Data Manipulation](https://store.metasnake.com/effective-pandas-book)** — Matt Harrison's book on writing idiomatic, readable pandas code, including method chaining. (GW users can look for it in [O'Reilly Online Learning](https://go.oreilly.com/gwu-edu).)

**Polars** is a newer DataFrame library (written in Rust, with a Python interface) designed for speed and for datasets that are large but still fit on one machine. It runs many times faster than pandas on big data, uses multiple CPU cores automatically, has a *lazy* mode that optimizes a whole query before running it, and can process data larger than memory in streaming mode. Its API is different from pandas — it is based on composable *expressions* (`pl.col("weight").mean()`) rather than an index — and many users find it more consistent and easier to read. Polars can convert to and from pandas DataFrames, so the two can be used together.

- **[Polars User Guide](https://docs.pola.rs/)** — The official guide, with a getting-started tour, an explanation of expressions and contexts, lazy vs. eager evaluation, and a "Coming from pandas" migration page.
- **[Polars: Coming from pandas](https://docs.pola.rs/user-guide/migration/pandas/)** — A side-by-side comparison of pandas and Polars idioms for people who already know pandas.
- **[Modern Polars](https://kevinheavey.github.io/modern-polars/)** — A free online book by Kevin Heavey that works through common data-analysis tasks in both pandas and Polars, side by side.
- **[Python Polars: The Definitive Guide](https://polarsguide.com/)** — The O'Reilly book by Jeroen Janssens and Thijs Nieuwdorp, the most complete treatment of Polars. (GW users can look for it in [O'Reilly Online Learning](https://go.oreilly.com/gwu-edu).)

**Which should I use?** Start with pandas if you are new to Python — it is what the tutorials, courses, and most colleagues use. Reach for Polars when your data are large (millions of rows), when pandas is too slow, or when you want the expression-based style. Two other options worth knowing about: **[DuckDB](https://duckdb.org/docs/stable/clients/python/overview.html)** lets you run fast SQL queries directly on pandas/Polars DataFrames and on CSV/Parquet files, and **[Dask](https://docs.dask.org/)** scales pandas-style code across many cores or a cluster (such as GW HPC) for data that do not fit on one machine.

---

## Advanced Python

- **[Think Python (3rd edition)](https://allendowney.github.io/ThinkPython/)** — Allen Downey's free online book goes deeper into how Python works: functions, recursion, classes and objects, inheritance, and program design, with a chapter-by-chapter set of Jupyter notebooks.
- **[Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)** — This free online book by Jake VanderPlas is a thorough tour of the core scientific Python stack: IPython/Jupyter, NumPy, pandas, matplotlib, and scikit-learn. Ideal for readers who already know basic Python and want to master the data-science libraries.
- **[Scientific Python Lectures](https://lectures.scientific-python.org/)** — Tutorials on the scientific Python ecosystem, from the language and NumPy through advanced topics such as optimization, image processing, and performance (Cython, profiling).
- **[Real Python](https://realpython.com/)** — A large collection of in-depth tutorials and video courses on Python topics at every level, from beginner concepts to packaging, testing, concurrency, and web development. Many tutorials are free.

---

## Python Practice

The fastest way to get comfortable with Python is to write a little of it regularly. These sites let you practice in your browser, with problems that check your answers, so you can build skills between workshops and courses.

Practice with real data:

- **[Programming with Python: Analyzing Patient Data (sandbox.bio)](https://sandbox.bio/tutorials/carpentries-python-inflammation)** — The Software Carpentry "inflammation" lesson, running entirely in your browser with nothing to install. You load a dataset of patients' daily inflammation measurements with NumPy, analyze and plot it with matplotlib, then learn loops, lists, conditionals, functions, error handling, and defensive programming along the way. (The original lesson, for use on your own computer, is at [swcarpentry.github.io/python-novice-inflammation](https://swcarpentry.github.io/python-novice-inflammation/).)
- **[Rosalind: Python Village](https://rosalind.info/problems/list-view/?location=python-village)** — Rosalind is a platform for learning bioinformatics through problem solving. The "Python Village" is its gentle introduction to Python — variables, strings, conditionals, loops, dictionaries, and file I/O — and each problem is checked automatically. Once you finish the Village, the [Bioinformatics Stronghold](https://rosalind.info/problems/list-view/) offers over 100 problems in DNA/RNA sequence analysis. You do not need to be a biologist to benefit from it.
- **[100 pandas puzzles](https://github.com/ajcr/100-pandas-puzzles)** and **[pandas exercises](https://github.com/guipsamora/pandas_exercises)** — Jupyter notebooks of short pandas exercises, from basics through grouping, merging, time series, and visualization, with solutions.
- **[Kaggle](https://www.kaggle.com/learn)** — In addition to its short courses, Kaggle offers thousands of [datasets](https://www.kaggle.com/datasets), free hosted notebooks, and beginner-friendly competitions (such as *Titanic*) for practicing data analysis and machine learning.

Practice the language:

- **[futurecoder](https://futurecoder.io/)** — A free, interactive course for complete beginners that runs in the browser, with a built-in editor, hints, and step-by-step debugging tools.
- **[Exercism: Python track](https://exercism.org/tracks/python)** — Over 100 free exercises organized by concept, with automated tests and optional feedback from volunteer mentors.
- **[Practice Python](https://www.practicepython.org/)** — Short beginner exercises, each with a walk-through solution — a good next step right after a first workshop.
- **[Python Morsels](https://www.pythonmorsels.com/)** — Weekly exercises (some free) with detailed explanations, aimed at moving from beginner to intermediate Python.
- **[Codewars](https://www.codewars.com/)** and **[HackerRank: Python](https://www.hackerrank.com/domains/python)** — Large collections of ranked coding challenges with automated checking; you can compare your solutions with others' after solving.
- **[Project Euler](https://projecteuler.net/)** — Hundreds of mathematical and computational problems, from easy to very hard, that reward clear thinking and efficient code.
- **[Advent of Code](https://adventofcode.com/)** — An annual series of daily puzzles each December (past years remain available); popular with the Python community and a fun way to build fluency.

Remember that the GW Libraries [Coding Consultations](https://calendly.com/gwul-coding) and Academic Commons [Data Consultations](http://go.gwu.edu/dataconsulting) are available if you get stuck.

---

## Python for Data Visualization

- **[matplotlib](https://matplotlib.org/stable/gallery/index.html)** — matplotlib is the foundational plotting library for Python. Its gallery displays hundreds of example charts along with their code so that you can reproduce them and adapt them to your own work. See also the official [matplotlib cheatsheets](https://matplotlib.org/cheatsheets/).
- **[seaborn](https://seaborn.pydata.org/tutorial.html)** — seaborn builds on matplotlib to provide a high-level interface for attractive statistical graphics — distributions, categorical plots, regression plots, and multi-panel figures — directly from pandas DataFrames.
- **[plotnine](https://plotnine.org/)** — plotnine is an implementation of the Grammar of Graphics in Python, based on R's ggplot2. If you already know ggplot2, or want to build plots layer by layer, this is the library for you.
- **[Plotly for Python](https://plotly.com/python/)** — Plotly creates interactive, web-based charts (hover, zoom, pan) with a concise `plotly.express` API, and is the plotting engine behind Dash apps.
- **[Vega-Altair](https://altair-viz.github.io/)** — A declarative visualization library, built on Vega-Lite, that lets you build interactive charts from a simple description of data, marks, and encodings.
- **[The Python Graph Gallery](https://python-graph-gallery.com/)** — With hundreds of examples organized by chart type, this collection displays charts along with their Python code (matplotlib, seaborn, plotly, and more).
- **[Fundamentals of Data Visualization](https://clauswilke.com/dataviz/)** — This online book by Claus Wilke is a language-agnostic guide to the principles of making clear, effective, and honest figures — which charts to use, how to use color, and what to avoid.

---

## Python for Statistics

- **[statsmodels](https://www.statsmodels.org/stable/index.html)** — statsmodels is the primary Python library for classical statistics: descriptive statistics, hypothesis tests, linear and generalized linear models, ANOVA, mixed-effects models, time series, and more, with R-style formulas and detailed summary tables.
- **[SciPy statistics (`scipy.stats`)](https://docs.scipy.org/doc/scipy/tutorial/stats.html)** — Probability distributions, summary statistics, correlation, and a wide range of statistical tests (t-tests, chi-square, nonparametric tests, and more).
- **[Pingouin](https://pingouin-stats.org/)** — A user-friendly statistics package built on pandas and SciPy that returns tidy, easy-to-read results for t-tests, ANOVAs, correlations, effect sizes, reliability, and more.
- **[Think Stats (3rd edition)](https://allendowney.github.io/ThinkStats/)** — Allen Downey's free online book introduces exploratory data analysis and statistical thinking using Python, with real datasets and Jupyter notebooks.
- **[An Introduction to Statistical Learning with Applications in Python](https://www.statlearning.com/)** — The Python edition of the classic textbook by James, Witten, Hastie, Tibshirani, and Taylor covers regression, classification, resampling, model selection, tree-based methods, and more, with free labs in Python.
- **[PyMC](https://www.pymc.io/)** — A library for Bayesian statistical modeling and probabilistic programming, with extensive examples and tutorials.

For predictive modeling and machine learning (scikit-learn, gradient boosting, deep learning), see *Python for Machine Learning*, below.

---

## Python for Authoring Documents and More

Jupyter notebooks and Quarto allow you to mix narrative and code to create reproducible documents, web sites, presentations, and more.

- **[Project Jupyter](https://jupyter.org/)** — The main site for Jupyter notebooks and JupyterLab: the interactive documents that combine live code, equations, visualizations, and narrative text. Notebooks can be exported to HTML, PDF, and slides.
- **[Quarto](https://quarto.org/docs/computations/python.html)** — Quarto is an open-source scientific and technical publishing system. It renders `.qmd` files or Jupyter notebooks into articles, reports, presentations, websites, books, and dashboards, and supports Python, R, Julia, and Observable JS.
- **[Jupyter Book](https://jupyterbook.org/)** — Build publication-quality books and documents from collections of notebooks and Markdown files, complete with cross-references, citations, and interactive outputs.
- **[marimo](https://marimo.io/)** — A newer reactive notebook for Python: cells re-run automatically when their inputs change, notebooks are stored as plain `.py` files, and they can be shared as interactive apps.

---

## Shiny, Streamlit, and Dash — Create Interactive Data Visualizations

Several Python frameworks let you create interactive web applications and dashboards from your data with no knowledge of HTML, CSS, or JavaScript.

- **[Shiny for Python](https://shiny.posit.co/py/)** — Posit's Shiny framework, now available for Python. Contains tutorials, a gallery of examples (with code), and how-to articles. Includes Shiny Express, a simplified syntax for getting started quickly.
- **[Streamlit](https://streamlit.io/)** — Turn a Python script into a shareable web app in minutes. Streamlit is especially popular for quick data dashboards and machine-learning demos; the [gallery](https://streamlit.io/gallery) has many examples with code.
- **[Dash](https://dash.plotly.com/)** — Plotly's framework for building analytical web applications and dashboards, with a large component library and a step-by-step tutorial.
- **[Panel](https://panel.holoviz.org/)** — A dashboarding library from the HoloViz project that works with nearly every Python plotting library and integrates well with Jupyter.

---

## Python for various applications

Text mining and natural language processing (NLP) with Python, tutorials:

- **[Natural Language Processing with Python (the NLTK Book)](https://www.nltk.org/book/)** — This free online book introduces text analysis using the Natural Language Toolkit: tokenizing, tagging, classifying text, extracting information, and analyzing linguistic structure.
- **[Advanced NLP with spaCy](https://course.spacy.io/)** — A free, interactive online course on using the spaCy library for modern NLP: named-entity recognition, part-of-speech tagging, rule-based matching, and training your own models.
- **[Hugging Face LLM Course](https://huggingface.co/learn/llm-course)** — A free course on using transformer models with the Hugging Face libraries for text classification, question answering, summarization, and more.
- **[The Programming Historian](https://programminghistorian.org/)** — A collection of novice-friendly, peer-reviewed tutorials to help humanists learn a wide range of digital tools, techniques, and workflows to facilitate research and teaching. Many of these tutorials use Python, covering topics such as text analysis, web scraping, working with APIs, and network analysis. Materials available in English, Spanish, French, and Portuguese.

Python for geospatial analysis, tutorials:

- **[Introduction to Geospatial Raster and Vector Data with Python](https://carpentries-incubator.github.io/geospatial-python/)** — This Carpentries lesson teaches how to work with geospatial data in Python: understanding spatial data formats and coordinate reference systems, and working with raster (rioxarray) and vector (GeoPandas) data for analysis and visualization.
- **[GeoPandas](https://geopandas.org/en/stable/getting_started.html)** — GeoPandas extends pandas to work with geographic data, making it easy to read shapefiles and GeoJSON, perform spatial joins and operations, and create maps.
- **[Geographic Data Science with Python](https://geographicdata.science/book/)** — This online book, by Sergio Rey, Dani Arribas-Bel, and Levi Wolf, introduces the concepts and tools of geographic data science in Python, including spatial data, spatial weights, exploratory spatial analysis, clustering, and spatial regression.
- **[Automating GIS Processes](https://autogis-site.readthedocs.io/)** — Course materials from the University of Helsinki on using Python for GIS: GeoPandas, coordinate systems, geocoding, spatial joins, network analysis, and map making.

Python for web scraping and working with APIs:

- **[Requests](https://requests.readthedocs.io/)** — The standard library for retrieving web pages and calling web APIs from Python.
- **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** — A library for parsing HTML and XML, commonly used to extract data from web pages. See also the web-scraping chapter of [Automate the Boring Stuff](https://automatetheboringstuff.com/).

Python can even be used to create generative art:

- **[py5](https://py5coding.org/)** — py5 brings the Processing creative-coding framework to Python, with tutorials for drawing, animation, and interactive sketches in Jupyter notebooks.
- **[Generative Art with Python (Processing.py tutorials)](https://py.processing.org/tutorials/)** — Tutorials from the Processing project on creating visual, generative art in Python.

Here are some great resources if you are looking for packages that might be useful in your analysis:

- **[PyPI — the Python Package Index](https://pypi.org/)** — The searchable catalog of over half a million Python packages that can be installed with `pip`.
- **[conda-forge](https://conda-forge.org/packages/)** — A community-maintained collection of packages installable with `conda`, especially useful for scientific libraries with compiled dependencies.
- **[Awesome Python](https://github.com/vinta/awesome-python)** — A curated list of well-regarded Python frameworks, libraries, and resources, organized by topic.

---

## Python for Machine Learning

Python is the dominant language for machine learning (ML): predicting an outcome from data (regression and classification), finding structure in data (clustering, dimensionality reduction), and, with deep learning, working with images, audio, and text. Most ML work begins with data in a pandas DataFrame and a train/test split, so the data-analysis skills above are the foundation.

For **classical machine learning** (linear and logistic regression, decision trees and random forests, gradient boosting, support-vector machines, k-means, PCA, and more):

- **[scikit-learn: Getting Started](https://scikit-learn.org/stable/getting_started.html)** and the **[scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)** — scikit-learn is the standard library for classical machine learning in Python. Every model uses the same `fit` / `predict` interface, and the library includes tools for preprocessing, cross-validation, hyperparameter tuning, pipelines, and evaluation metrics. The user guide doubles as a well-written introduction to each method.
- **[An Introduction to Statistical Learning with Applications in Python](https://www.statlearning.com/)** — The Python edition of the classic textbook (James, Witten, Hastie, Tibshirani, and Taylor) explains the statistical ideas behind ML methods, with free labs using scikit-learn and statsmodels. Free PDF and companion videos.
- **[Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow (3rd edition)](https://github.com/ageron/handson-ml3)** — Aurélien Géron's widely used, project-based book; the companion Jupyter notebooks are free on GitHub, and GW users can read the full book in [O'Reilly Online Learning](https://go.oreilly.com/gwu-edu).
- **[XGBoost](https://xgboost.readthedocs.io/)** and **[LightGBM](https://lightgbm.readthedocs.io/)** — Gradient-boosted tree libraries that are often the best-performing choice for tabular data; both work with scikit-learn pipelines.
- **[Kaggle Learn](https://www.kaggle.com/learn)** — Short, free, hands-on courses (Intro to Machine Learning, Intermediate ML, Feature Engineering, and more) that run in your browser.

For **deep learning** (neural networks for images, audio, text, and other complex data):

- **[PyTorch tutorials](https://pytorch.org/tutorials/)** — Official tutorials for PyTorch, the most widely used deep-learning framework in research. Start with "Learn the Basics."
- **[Practical Deep Learning for Coders (fast.ai)](https://course.fast.ai/)** — A free course that teaches deep learning from a practical, top-down perspective, using PyTorch and the fastai library. You build working models in the first lesson.
- **[Deep Learning with PyTorch: A 60 Minute Blitz](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)** — A fast introduction to tensors, autograd, and training a classifier.
- **[TensorFlow / Keras tutorials](https://www.tensorflow.org/tutorials)** — The other major deep-learning framework; Keras provides a high-level, beginner-friendly API.
- **[Dive into Deep Learning](https://d2l.ai/)** — A free, interactive online textbook (with code in PyTorch, TensorFlow, and JAX) used at many universities, covering everything from linear regression to transformers.

Training deep-learning models often requires a GPU. [Google Colab](https://colab.research.google.com/) provides free (limited) GPU access, and GW researchers can request access to GPU nodes on [GW High Performance Computing (HPC)](https://it.gwu.edu/hpc).

---

## Python for AI and Large Language Models

Python is the primary language for building with and studying large language models (LLMs) and other generative AI tools: calling models such as Claude and GPT from code, running open-weight models on your own computer, classifying or extracting information from thousands of documents, building chatbots and research assistants over your own materials (Retrieval-Augmented Generation, or RAG), and fine-tuning models.

**Calling hosted LLMs from Python** (you write code that sends prompts to a model and receives responses):

- **[Anthropic Python SDK](https://docs.claude.com/en/api/client-sdks)** — The official client library for Claude, with documentation on the Messages API, tool use, and structured outputs.
- **[OpenAI Python library](https://github.com/openai/openai-python)** — The official client library for OpenAI models.
- **[chatlas](https://posit-dev.github.io/chatlas/)** — chatlas, from Posit, provides a simple, unified interface for chatting with LLMs from many providers (Anthropic, OpenAI, Google, Ollama, and more). It is the Python counterpart to R's ellmer and is a good place to start for researchers.
- **[LiteLLM](https://docs.litellm.ai/)** — Call over 100 LLM providers through one OpenAI-compatible interface, so you can switch models without rewriting code.

**Running open-weight models locally** (no API costs, and your data never leave your machine — important for sensitive research data):

- **[Ollama](https://ollama.com/)** and the **[Ollama Python library](https://github.com/ollama/ollama-python)** — The easiest way to download and run open models (Llama, Mistral, Gemma, Qwen, and others) on your own computer and call them from Python.
- **[Hugging Face Transformers](https://huggingface.co/docs/transformers/index)** — Download and run thousands of open pretrained models for text, vision, and audio from the [Hugging Face Hub](https://huggingface.co/models), and fine-tune them on your own data.
- **[Hugging Face LLM Course](https://huggingface.co/learn/llm-course)** — A free course on using transformer models with the Hugging Face libraries for text classification, question answering, summarization, and more.
- **[vLLM](https://docs.vllm.ai/)** — A high-throughput serving engine for running open models at scale on GPU hardware such as GW HPC.

**Building applications: RAG, agents, and structured extraction:**

- **[LangChain](https://python.langchain.com/)** and **[LlamaIndex](https://docs.llamaindex.ai/)** — Frameworks for building LLM-powered applications, including Retrieval-Augmented Generation (RAG) workflows that let a model answer questions using your own documents.
- **[Pydantic AI](https://ai.pydantic.dev/)** — A framework for building agents and getting reliable, type-checked structured output from LLMs — useful for extracting data from text at scale.
- **[Instructor](https://python.useinstructor.com/)** — A lightweight library for getting structured (JSON / Pydantic) output from many LLM providers.
- **[Chroma](https://docs.trychroma.com/)** — An open-source vector database for storing document embeddings, a key building block of RAG systems.
- **[Gradio](https://www.gradio.app/)** — Quickly build a shareable web interface (a chat box, an upload form) around a model or a Python function with a few lines of code.

**Understanding how LLMs work:**

- **[Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)** — Andrej Karpathy's free video course builds neural networks and a GPT from scratch in Python, step by step.
- **[Build a Large Language Model (From Scratch)](https://github.com/rasbt/LLMs-from-scratch)** — Sebastian Raschka's book and companion notebooks implement a GPT-style model in PyTorch; the code is free on GitHub, and GW users can read the book in [O'Reilly Online Learning](https://go.oreilly.com/gwu-edu).
- **[Hugging Face Learn](https://huggingface.co/learn)** — Free courses on LLMs, agents, computer vision, audio, and reinforcement learning.
- **[Prompt Engineering Guide](https://www.promptingguide.ai/)** — A guide to prompting techniques, with examples and links to the research literature.

**Responsible use in research.** Before sending research data to a hosted AI service, check whether the data are sensitive or restricted (human-subjects data, FERPA-protected records, unpublished data under a data-use agreement); running models locally or on GW infrastructure may be required. GW's guidance on generative AI tools is at [it.gwu.edu/ai](https://it.gwu.edu/ai). LLM outputs can be confidently wrong — validate a sample of results by hand, report the model and version you used, and keep your prompts and code so your analysis is reproducible.

---

## Python Learning Resources and Communities

- **[LinkedIn Learning](https://go.gwu.edu/linkedinlearning)** — LinkedIn Learning offers video-based learning on a variety of coding topics, including Python. GW users will be prompted to log in with GW credentials. LinkedIn Learning offers dozens of courses on Python programming and data analysis with Python.
- **[O'Reilly Online Learning](https://go.oreilly.com/gwu-edu)** — Online collection of ebooks, videos, and learning paths including many about Python programming (including full-text access to books such as *Python for Data Analysis*, *Fluent Python*, and *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*). GW users will be prompted to log in using GW credentials in order to access this resource.
- **[PyCon US talk recordings](https://www.youtube.com/@PyConUS)** — Video recordings of talks and tutorials from PyCon US, the largest annual gathering of the Python community.
- **[SciPy conference recordings](https://www.youtube.com/@enthought)** — Talks and tutorials from the annual SciPy conference on scientific computing with Python.
- **[DC Python Meetup](https://www.meetup.com/dcpython/)** — The Washington, D.C. Python user group, which hosts regular talks, project nights, and social events.
- **[PyLadies DC](https://www.meetup.com/dc-pyladies/)** — The Washington, D.C. chapter of PyLadies, an international mentorship group with a focus on helping more women become active participants and leaders in the Python community.
- **[PyData](https://pydata.org/)** — A community of users and developers of open-source data tools, with meetups (including PyData DC) and conferences worldwide.
- **[Python Discord](https://www.pythondiscord.com/)** — A large, friendly online community for Python learners at all levels, with dedicated help channels.
- **[pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)** — A two-page reference to the most common pandas operations for data wrangling; see also the official [matplotlib cheatsheets](https://matplotlib.org/cheatsheets/).
- **[Python Software Foundation community page](https://www.python.org/community/)** — Mailing lists, forums, IRC/Discord channels, local user groups, and conferences.
