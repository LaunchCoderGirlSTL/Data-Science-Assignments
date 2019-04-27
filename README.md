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

## In Class Assignment due Friday, March 15, 2019 @ 8pm
* Readings & video
    - [Bootstrapping introduction](https://statisticsbyjim.com/hypothesis-testing/bootstrapping/)
    - [Bootstrapping video](https://www.youtube.com/watch?v=gcPIyeqymOU)

# Week 9
## Homework due Wednesday March 20, 2019 @ 6pm
* [Coursera Machine Learning](https://www.coursera.org/learn/machine-learning) 
    - Enroll in Coursera's Machine Learning Cohort that starts on March 18th: [Coursera Machine Learning](https://www.coursera.org/learn/machine-learning) You will be able to access lecture material today.
    - Finish all Readings, Videos, and Quizzes for the following sections in [Week 1: Introduction](https://www.coursera.org/learn/machine-learning/home/week/1):
        - [Introduction](https://www.coursera.org/learn/machine-learning/home/week/1)
        - [Linear Regression with One Variable](https://www.coursera.org/learn/machine-learning/home/week/1)

* [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)
    - Enroll in Google's Machine Learning Crash course. The material is available antyime. [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course/)
    - Finish all Videos, Readings, Key Terminology, and Check Your Understanding for the following sections:
        - [Introduction to ML](https://developers.google.com/machine-learning/crash-course/ml-intro)
        - [Framing](https://developers.google.com/machine-learning/crash-course/framing/video-lecture)
        - [Descending into ML](https://developers.google.com/machine-learning/crash-course/descending-into-ml/video-lecture)
        - [Reducing Loss](https://developers.google.com/machine-learning/crash-course/reducing-loss/video-lecture)

* [Introduction to Machine Learning with Python](https://github.com/amueller/introduction_to_ml_with_python)
    - Clone or download (click the green `Clone or Download` button) the entire [Introduction to Machine Learning with Python](https://github.com/amueller/introduction_to_ml_with_python) GitHub Repo. Ensure that all appropriate packages are installed on your computer before class Wednesday March 20th. We will be following through these notebooks as our In-Class Assignments. 
    
* [HackerRank](https://www.hackerrank.com/domains/mathematics?filters%5Bsubdomains%5D%5B%5D=linear-algebra-foundations)
    - Solve the following HackerRank Linear Algebra Problems:
        - [Linear Algebra Foundations #1 - Matrix Addition](https://www.hackerrank.com/challenges/linear-algebra-foundations-1/problem)
        - [Linear Algebra Foundations #2 - Matrix Subtraction](https://www.hackerrank.com/challenges/linear-algebra-foundations-1-matrix-subtraction/problem)
        - [Linear Algebra Foundations #3 - Matrix Multiplication](https://www.hackerrank.com/challenges/linear-algebra-foundations-3-matrix-multiplication/problem)
        - [Linear Algebra Foundations #4 - Matrix Multiplication](https://www.hackerrank.com/challenges/linear-algebra-foundations-4-matrix-multiplication/problem)
    - If you have trouble with any of the problems above, check out some of the review material on Khan Academy:
        - [Adding vectors algebraically & graphically](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/vectors/v/adding-vectors)
        - [Vector Examples](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/vectors/v/linear-algebra-vector-examples)
 
 
## In Class Assignment due Friday, March 22, 2019 @ 8pm
* [Introduction to Machine Learning with Python](https://github.com/amueller/introduction_to_ml_with_python)
    - Work through [Introduction to ML Notebook](https://github.com/amueller/introduction_to_ml_with_python/blob/master/01-introduction.ipynb)
* Bootstrapping Followup 
    - Work through [Bootstrapping Notebook](https://github.com/rasbt/data-science-tutorial/blob/master/code/bootstrapping.ipynb)
    
    
# Week 10
## Homework due Wednesday March 27, 2019 @ 6pm
* [Coursera Machine Learning](https://www.coursera.org/learn/machine-learning) 
    - Finish all Readings, Videos, and Quizzes for the following sections in [Week 1](https://www.coursera.org/learn/machine-learning/home/week/1) and [Week 2](https://www.coursera.org/learn/machine-learning/home/week/2):
        - [Linear Algebra Review](https://www.coursera.org/learn/machine-learning/home/week/1)
        - [Linear Regression with Multiple Variables](https://www.coursera.org/learn/machine-learning/home/week/2)

* [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)
    - If you didn't complete all items in Week 9 (__including Playground Exercises__) in [Introduction to ML](https://developers.google.com/machine-learning/crash-course/ml-intro), [Framing](https://developers.google.com/machine-learning/crash-course/framing/video-lecture), [Descending into ML](https://developers.google.com/machine-learning/crash-course/descending-into-ml/video-lecture), or [Reducing Loss](https://developers.google.com/machine-learning/crash-course/reducing-loss/video-lecture), go back and finish all items.
    - Finish all Videos, Readings, Key Terminology, Playground Exercises, __Programming Assignments__, and Check Your Understanding for the following sections. 
        - [First Steps with TF](https://developers.google.com/machine-learning/crash-course/first-steps-with-tensorflow/video-lecture): There's are 3 _Programming Assignments_ with this section which will run on [Google's Colaboratory](https://colab.research.google.com/) platform. These are very similar to Jupyter notebooks, but will *not* run locally.  
            - Quick Introduction to pandas
            - First Steps with TensorFlow
            - Synthetic Features and Outliers
        - [Generalization](https://developers.google.com/machine-learning/crash-course/generalization/)
        - [Training and Test Sets](https://developers.google.com/machine-learning/crash-course/training-and-test-sets/video-lecture)
        
## In Class Assignment due Friday, March 29, 2019 @ 8pm
* [Introduction to Machine Learning with Python](https://github.com/amueller/introduction_to_ml_with_python)
    - Work through [Supervised Learning Notebook](https://github.com/amueller/introduction_to_ml_with_python/blob/master/02-supervised-learning.ipynb) _through only Section:_ __Linear regression aka ordinary least squares__ This is a very long notebook and we will be working through the ML algorithms week-by-week. 

# Week 11
## Homework due Wednesday April 3, 2019 @ 6pm
* [Coursera Machine Learning](https://www.coursera.org/learn/machine-learning) 
    - Finish all Readings, Videos, and Quizzes for the following sections in [Week 3](https://www.coursera.org/learn/machine-learning/home/week/3):
        - [Logisitic Regression](https://www.coursera.org/learn/machine-learning/home/week/3)
        - [Regularization](https://www.coursera.org/learn/machine-learning/home/week/3)

* [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)
    - Finish all Videos, Readings, Key Terminology, Playground Exercises, and Check Your Understanding for the following sections:
        - [Training and Test Sets](https://developers.google.com/machine-learning/crash-course/training-and-test-sets/video-lecture)
        - [Validation Set](https://developers.google.com/machine-learning/crash-course/validation/check-your-intuition)
        - [Regularization for Simplicity](https://developers.google.com/machine-learning/crash-course/regularization-for-simplicity/playground-exercise-overcrossing)
        - [Logistic Regression](https://developers.google.com/machine-learning/crash-course/logistic-regression/video-lecture)
* [Harvard CS109](https://github.com/cs109/content)
    - Work through [Bias, Variance, Cross-Validation](https://nbviewer.jupyter.org/github/cs109/content/blob/master/labs/lab5/Lab5.ipynb) Notebook

## In Class Assignment due Friday, April 5, 2019 @ 8pm
*  [Harvard CS109](https://github.com/cs109/content)
    - Work through [Sklearn, Regression, PCA](https://nbviewer.jupyter.org/github/cs109/content/blob/master/labs/lab4/Lab4full.ipynb) Notebook
    
# Week 12
## Homework due Wednesday April 10, 2019 @ 6pm
*  Catch up Week! :) Make sure that you are caught up on all assignments through the Week 11 In Class Assignment

# Week 13
## Homework due Wednesday April 17, 2019 @ 6pm
* [Coursera Machine Learning](https://www.coursera.org/learn/machine-learning) 
    - Finish all Readings, Videos, and Quizzes for the following sections in [Week 4](https://www.coursera.org/learn/machine-learning/home/week/4):
        - [Neural Networks: Representation](https://www.coursera.org/learn/machine-learning/home/week/4)

* [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)
    - Finish all Videos, Readings, Key Terminology, Playground Exercises, and Check Your Understanding for the following sections:
        - [Representation](https://developers.google.com/machine-learning/crash-course/representation/video-lecture)
        - [Feature Crosses](https://developers.google.com/machine-learning/crash-course/feature-crosses/video-lecture)
        
## In Class Assignment due Wednesday April 24th, 2019 @ 6pm
* Work through [Dense NN MINST Notebook](https://github.com/cschlosberg/codergirl-python/blob/master/Dense-NN-MINST_clean.ipynb)

# Week 14
## Homework due Wednesday April 24th, 2019 @ 6pm
* [Coursera Machine Learning](https://www.coursera.org/learn/machine-learning) 
    - Finish all Readings, Videos, and Quizzes for the following sections in [Week 5](https://www.coursera.org/learn/machine-learning/home/week/5):
        - [Neural Networks: Learning](https://www.coursera.org/learn/machine-learning/home/week/5)

* [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)
    - Finish all Videos, Readings, Key Terminology, Playground Exercises, and Check Your Understanding for the following sections:
        - [Neural Networks](https://developers.google.com/machine-learning/crash-course/representation/video-lecture)
        - [Training Neural Networks](https://developers.google.com/machine-learning/crash-course/introduction-to-neural-networks/video-lecture)

## In Class Assignment
* No In-Class Assignment due. Make sure to finish Week 13 In Class Assignment

## Deep Learning Specialization
* For those of you interested in learning more in-depth material about Neural Networks, we highly recommend you to complete the [Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning). This is a 5 course series from Coursera which deals with implementing a set of state-of-the-art Neural Networks. This is well beyond the scope of CoderGirl- Data Science, but we wanted to keep this here as a reference. 

# Week 15
## Homework due Wednesday May 1st, 2019 @ 6pm
* [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course/)
    - Finish all Videos, Readings, Key Terminology, Playground Exercises, and Check Your Understanding for the following sections:
        - [Classification](https://developers.google.com/machine-learning/crash-course/classification/video-lecture)
        - [Regularization: Sparsity](https://developers.google.com/machine-learning/crash-course/regularization-for-sparsity/video-lecture)
        - [Mutli-Class Neural Networks](https://developers.google.com/machine-learning/crash-course/multi-class-neural-networks/video-lecture)
