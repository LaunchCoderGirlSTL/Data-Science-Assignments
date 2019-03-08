# Data-Science-Assignments
Repository for the Data Science learning track to host assignments.

# Week 1
## In Class Assignment due Saturday Jan 26, 2019 @ 8pm
* Readings (The Unix Shell)
    - [Introducing the Shell](http://swcarpentry.github.io/shell-novice/01-intro/index.html)
    - [Navigating Files and Directories](http://swcarpentry.github.io/shell-novice/02-filedir/index.html)
    - [Working with Files and Directories](http://swcarpentry.github.io/shell-novice/03-create/index.html)
    - [Pipes and Filters](http://swcarpentry.github.io/shell-novice/04-pipefilter/index.html)

# Week 2
## Homework due Wednesday Jan 30, 2019 @ 6pm
* Readings
    - [Hello World tutorial](https://www.learnpython.org/en/Hello,_World!)
    - [Data types & data structures](https://www.datacamp.com/community/tutorials/data-structures-python)
    - [String manipulations](http://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-12--string-manipulation)
    - [If-else](https://www.w3schools.com/python/python_conditions.asp)
    
* Signup for Hackerrank and complete the following Hackerrank challenges.
    - [Python Hello World](https://www.hackerrank.com/challenges/py-hello-world/problem)
    - [Basic math](https://www.hackerrank.com/challenges/python-division/problem)
    - [String manipulations](https://www.hackerrank.com/challenges/python-string-split-and-join/problem)
    - [String manipulations 2](https://www.hackerrank.com/challenges/python-mutations/problem)
    - [Python If-Else](https://www.hackerrank.com/challenges/py-if-else/problem)
    
* Setup & configure git
    - Create a [GitHub](https://github.com/) account.
    - [Create an SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/).
    - [Link your SSH key to your GitHub account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
    - [Verify](https://help.github.com/articles/testing-your-ssh-connection/) your SSH connection.
    
## In Class Assignment due Friday Feb 1, 2019 @ 8pm
* Finish working through the [Intro to Python notebook](http://nbviewer.jupyter.org/github/rlowd/python-bigdata/blob/master/src/main/ipynb/intro-python-scrubbed.ipynb).
    - Note this version has no "answers" -- none of the cells are executed. You can work through all the sections, but minimally work through the code blocks we didn't get through Wednesday night.

# Week 3
## Homework due Wednesday Feb 6, 2019 @ 6pm
* Readings
    - [Loops](https://www.datacamp.com/community/tutorials/loops-python-tutorial)
    - [Functions](https://www.datacamp.com/community/tutorials/functions-python-tutorial)
    - [Modulo documentation](https://python-reference.readthedocs.io/en/latest/docs/operators/modulus.html)
        - Supplemental (not required): [Modulo video](https://www.youtube.com/watch?v=ythAmIKawv0). You'll need to use the *modulo* operator for one of your homeworks. If the documentation below isn't enough to help you solve the challenge, see the video as well.
    - [List comprehensions](https://www.datacamp.com/community/tutorials/python-list-comprehension)
        - Supplemental (not required): [more on list comprehensions](https://www.python-course.eu/python3_list_comprehension.php)
    - [Lambda functions & map, filter, reduce](https://www.python-course.eu/python3_lambda.php)
    
* Cheat Sheets
    - [Jupyter notebooks](https://datacamp-community-prod.s3.amazonaws.com/48093c40-5303-45f4-bbf9-0c96c0133c40)
    - [Python for Data Science](https://datacamp-community-prod.s3.amazonaws.com/e30fbcd9-f595-4a9f-803d-05ca5bf84612)
        
* Hackerrank Python
    - [Loops](https://www.hackerrank.com/challenges/python-loops/problem)
    - [List comprehensions](https://www.hackerrank.com/challenges/list-comprehensions/problem)
        - The Problem statement and Tutorial should be sufficient to guide you through this exercise, but the example code using list comprehensions on the Problem page is difficult to read. Here it is line by line (and in Python3):
        __Code using list comprehensions:__  
        `x = int( raw_input() )`  
        `y = int( raw_input() )`  
        `n = int( raw_input() )`  
        `print( [ [i, j] for i in range(x + 1) for j in range(y + 1) if( ( i + j ) != n )] )`  
    - [Your first Python function](https://www.hackerrank.com/challenges/whats-your-name/problem)
        - Bonus: Try testing your code against custom input (your name!).
    - [More functions](https://www.hackerrank.com/challenges/write-a-function/problem?h_r=next-challenge&h_v=zen)
    - Bonus (not required): [Nested lists](https://www.hackerrank.com/challenges/nested-list/problem)


## In Class Assignment due Friday Feb 8, 2019 @ 8pm
* Finish working through the [Intro to Python 2 notebook](https://github.com/rlowd/python-bigdata/blob/master/src/main/ipynb/intro-python-2-scrubbed.ipynb)

# Week 4
## Homework due Wednesday Feb 13, 2019 @ 6pm
* Readings
    - [Type conversion](https://www.datacamp.com/community/tutorials/python-data-type-conversion)
    - [Numpy overview](https://www.datacamp.com/community/tutorials/python-numpy-tutorial)
        - Note: You won't need to install numpy (it should be included with your Anaconda installation). 

* Jupyter notebooks
    - [Tutorial: Computing with NumPy arrays](https://github.com/rlowd/python-bigdata/blob/master/ipython-minibook/numpy-computing.ipynb). You can download the data and execute the code in this notebook yourself, or just read through the executed version. Make sure you understand all the `numpy` methods.

* Cheat Sheets
    - [NumPy](https://datacamp-community-prod.s3.amazonaws.com/e9f83f72-a81b-42c7-af44-4e35b48b20b7)

* Hackerrank
    - [Numpy arrays](https://www.hackerrank.com/challenges/np-arrays/problem)
    - [Zeros and ones](https://www.hackerrank.com/challenges/np-zeros-and-ones/problem)
    - [Vector math](https://www.hackerrank.com/challenges/np-array-mathematics/problem)
    - [Min and max](https://www.hackerrank.com/challenges/np-min-and-max/problem)
    - [Floor/ceiling/rint](https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem)
    - [Reshape arrays](https://www.hackerrank.com/challenges/np-shape-reshape/problem)

## In Class Assignment due Friday Feb 15, 2019 @ 8pm
* Finish working through the [Numerical computing notebook](https://github.com/rlowd/python-bigdata/blob/master/src/main/ipynb/numerical-slides-scrubbed.ipynb) and the associated readings (linked in the notebook).

# Week 5
## Homework due Wednesday Feb 20, 2019 @ 6pm
* Readings
    - [Pandas DataFrames](https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python)
    - [Time Series tutorial with Pandas](https://www.datacamp.com/community/tutorials/time-series-analysis-tutorial)
    - [Matplotlib tutorial](https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python)
    - Notebooks to read through:
        - Pulling data & assembling Pandas DataFrame - [Chipotle dataset](https://github.com/rlowd/python-bigdata/blob/master/pandas-exercises/chipotle-getting-and-knowing-read-only.ipynb)
        - Exploratory analysis with `matplotlib` - [Retail dataset](https://github.com/rlowd/python-bigdata/blob/master/pandas-exercises/online-retail-plotting.ipynb)

* Coding challenges: 
    - Notebooks with fill-in-the-blank code blocks - _will be posted by 12p Friday, Feb 15_.
        - Reading in & assembling Pandas Data Frames - [Occupations dataset](https://github.com/rlowd/python-bigdata/blob/master/pandas-exercises/occupations/occupation-getting-and-knowing-blanks-scrubbed.ipynb)
            - [Executed](https://github.com/rlowd/python-bigdata/blob/master/pandas-exercises/occupations/occupation-getting-and-knowing-blanks-with-solutions.ipynb) but no solutions.
        - Plotting practice - [Titanic dataset](https://github.com/rlowd/python-bigdata/blob/master/pandas-exercises/titanic/titanic-plotting-blanks-scrubbed.ipynb)
            - [Executed](https://github.com/rlowd/python-bigdata/blob/master/pandas-exercises/titanic/titanic-plotting-blanks-with-solutions.ipynb) but no solutions.
    - Hackerrank
        - [Numpy array stats](https://www.hackerrank.com/challenges/np-mean-var-and-std/problem)
        - [Floating point practice](https://www.hackerrank.com/challenges/introduction-to-regex/problem)
        - [Working with integers](https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem)

## In Class Assignment due Friday Feb 22, 2019 @ 8pm
* Work through ONE notebooks:
    - More plotting practice - [tips notebook](https://github.com/rlowd/python-bigdata/blob/master/pandas-exercises/tips/tips-plotting-blanks-scrubbed.ipynb)
        - [Executed](https://github.com/rlowd/python-bigdata/blob/master/pandas-exercises/tips/tips-plotting-blanks-executed.ipynb)

# Week 6
## Homework due Wednesday Feb 27, 2019 @ 6pm
* Readings
    - [Think Stats: Chapter 1 - Exploratory Data Analysis](http://greenteapress.com/thinkstats2/thinkstats2.pdf)
    - [Exploratory Data Analysis I](https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python)
    - [Exploratory Data Analysis II](https://www.datacamp.com/community/tutorials/python-data-profiling)
    - [Hierarchical Indicies, Groupby](https://www.datacamp.com/community/tutorials/pandas-multi-index)
    - [Think Stats: Chapter 2 - Distributions](http://greenteapress.com/thinkstats2/thinkstats2.pdf)

* Cheat Sheets
    - [Pandas](https://datacamp-community-prod.s3.amazonaws.com/fbc502d0-46b2-4e1b-b6b0-5402ff273251)

* Hackerrank
    - [Statistics Warmup](https://www.hackerrank.com/challenges/stat-warmup/problem)

* Jupyter Notebooks
    - [Pandas Groupby](https://github.com/cschlosberg/codergirl-python/blob/master/pandas-groupby.ipynb)
    - [Pandas Apply](https://github.com/cschlosberg/codergirl-python/blob/master/pandas-apply.ipynb)
    - [Pandas Stats](https://github.com/cschlosberg/codergirl-python/blob/master/pandas-stats.ipynb)
    - [Pandas Visualization](https://github.com/cschlosberg/codergirl-python/blob/master/pandas-visualization.ipynb)

## In Class Assignment due Friday Mar 1, 2019 @ 8pm
* Read through and run commands for following tutorials:
    - [Seaborn Introduction](https://elitedatascience.com/python-seaborn-tutorial)
    - [Seaborn Tutorial](https://nbviewer.jupyter.org/github/jdwittenauer/ipython-notebooks/blob/master/notebooks/libraries/Seaborn.ipynb)

# Week 7
## Homework due Wednesday March 6, 2019 @ 6pm
* Reading
    - [ThinkStats](http://greenteapress.com/thinkstats2/thinkstats2.pdf)
        - Chapters 3-5. Don't worry about the `thinkplot` code or the exercises at the end of each chapter. Focus on the content! The goal is to be familiar with different types of distributions.
        
* Watch
    - Videos on [normal distributions](https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/normal-distributions-library/v/ck12-org-normal-distribution-problems-qualitative-sense-of-normal-distributions).
        - Work through [practice exercises](https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/normal-distributions-library/e/empirical_rule).
        - Understand the [review page](https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/normal-distributions-library/a/normal-distributions-review).

* Notebooks
    - Download and work through the following 3 notebooks. Make sure you understand the concepts as well as the python code. You should complete the exercises throughout.
        - [Warm-up](https://github.com/rlowd/python-bigdata/blob/master/intro2stats/notebooks/2.%20Warm-up.py3.ipynb).
        - [Baisc Metrics](https://github.com/rlowd/python-bigdata/blob/master/intro2stats/notebooks/4.%20Basic%20Metrics.py3.ipynb)
        - [Distributions](https://github.com/rlowd/python-bigdata/blob/master/intro2stats/notebooks/5.%20Distributions.py3.ipynb)
        - [Directory with datasets](https://github.com/rlowd/python-bigdata/tree/master/intro2stats/data) for the above 3 notebooks. You should download these data to the same directory where the notebooks are. You will need to provide the correct path to your data in each Jupyter Notebook.

## In Class Assignment due Friday, March 8, 2019 @ 8pm
* Readings
    - [Groupby documentation](https://pandas.pydata.org/pandas-docs/version/0.22/groupby.html) - this entire page is really good, but read at least the first two sections ("Splitting an object into groups" and "Aggregation," up to the "Transformation" section).
        - Relevant to class Wednesday: [attributes for GroupBy objcets](https://pandas.pydata.org/pandas-docs/version/0.22/groupby.html#groupby-object-attributes) (e.g. how we found you can call `head` on a GroupBy object).
        - For in-class assignment: [Iterating through groups](https://pandas.pydata.org/pandas-docs/version/0.22/groupby.html#iterating-through-groups).
        
* Complete blank code blocks in [groupby notebook](https://github.com/rlowd/python-bigdata/blob/master/pandas-exercises/groupby-practice/regiment-executed-blanks.ipynb).

# Week 8
## Homework due Wednesday March 13, 2019 @ 6pm
* Readings
    - [ThinkStats](http://greenteapress.com/thinkstats2/thinkstats2.pdf)
        - Chapters 6-8. Don't worry about the `thinkplot` code or the exercises at the end of each chapter. Focus on the content! 
    - Bootstrapping -- _coming_
    
* Kahn Academy
    - Probabilities
        - Take [this quiz](https://www.khanacademy.org/math/statistics-probability/probability-library/modal/e/probability_1). If you have trouble with the answers, please watch the videos for the [basic probability](https://www.khanacademy.org/math/statistics-probability/probability-library#basic-theoretical-probability) section.
        - Videos, articles & quizzes for [Experimental probability](https://www.khanacademy.org/math/statistics-probability/probability-library#experimental-probability-lib).
        - Videos, articles & quizzes for [Randomness, probability & simulation](https://www.khanacademy.org/math/statistics-probability/probability-library#randomness-probability-and-simulation).
    - Hypothesis testing
        - Videos & quizzes for [Significance tests](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample#idea-of-significance-tests).
    - Scatterplots & correlations
        - Videos, articles & quizzes for [Introduction to scatterplots](https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data#introduction-to-scatterplots).
        - Videos, articles & quizzes for [Correlation](https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data#scatterplots-and-correlation)
    
* Notebooks
    - [Hypothesis testing](https://github.com/rlowd/python-bigdata/blob/master/intro2stats/notebooks/Hypothesis-Testing-executed-no-solutions.ipynb)
    
* Hackerrank
    - Write _only_ your *pseudocode* solution for this challenge: [Expected value & variance](https://www.hackerrank.com/challenges/dice-stats/problem) of a weighted die.
