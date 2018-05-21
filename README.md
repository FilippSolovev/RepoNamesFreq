# RepoNamesFreq
RepoNamesFreq clones a remote GitHub repository to the temporary location and then performs simple frequency analysis of words (either nouns or verbs) that have been used in naming python functions/methods or local variables.

# Example

To make it work on this particular repository type the following:

~~~~
$ python reponamesfreq.py -u https://github.com/FilippSolovev/RepoNamesFreq.git -s func -wt noun -o csv
The repository has been successfully cloned
total 5 files
trees generated
total 16 functions
total 35 words, 26 unique
~~~~

The arguments in the example above stands for:

* -u or --url specifies url of a remote repository, if it's omitted the script will look for .py files in the current working directory
* -s or --source tells the script what an object of analysis is, it can be 'func' or 'var', defining function names or variable names respectively. By default, it will process function names
* -wt or --wordtype can be either 'verb' or 'noun,' in case of absence the script will count verbs.
* -o or --output makes it possible to choose how results will be presented - a .json or .csv file in the current directory (with 'json' or 'csv' correspondingly) or just ten most frequent words in console output (showed below) if the argument was neglected.

An example of console output:
~~~~
list 4
fetch 3
names 3
words 2
visit 2
check 1
word 1
type 1
parse 1
snake 1
~~~~

# Installation

Clone the project and install the requirements:

~~~~
$ git clone https://github.com/FilippSolovev/RepoNamesFreq
$ pip install -r requirements.txt
~~~~

Since the project uses NLTK it needs ‘averaged_perceptron_tagger’, to obtain this resource use [NLTK Downloader](https://www.nltk.org/data.html "NLTK Downloader") typing in python:

~~~~
>>> import nltk
>>> nltk.download('averaged_perceptron_tagger')
~~~~

See NLTK documentation for details.

# Built With
* [GitPython](https://gitpython.readthedocs.io/en/stable/ "GitPython") - for cloning GitHub repositories
* [Abstract Syntax Trees](https://greentreesnakes.readthedocs.io/en/latest/index.html "AST") - for inspecting Python code
* [NLTK](https://www.nltk.org "NLTK") - for parsing function and variable names 

For in-depth NLTK understanding see [Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.](https://www.nltk.org/book/ "Natural Language Processing with Python").

# Authors
[FilippSolovev](https://github.com/FilippSolovev "FilippSolovev")

# License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/FilippSolovev/RepoNamesFreq/blob/master/LICENSE) file for details
