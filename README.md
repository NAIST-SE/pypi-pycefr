# **pycefrl**
## *Identifying Python3 Code Level Using the CERFL Framework as Inspiration*

### What is this project about?
The goal of pycefrl is to create a tool capable of obtaining an evaluation inspired by the [''Common European Framework of Reference for Languages''](https://en.wikipedia.org/wiki/Common_European_Framework_of_Reference_for_Languages) for code written in the Python programming language, version 3.

With this tool it is possible to analyze the level of GitHub repositories (and their developers) or code snippets in Python3.

### How does it work?

from pycefr import pycerfl
from pycefr import getcsv as pd2
import os

pycerfl.read_Directory('C:/Users/raula/Documents/GitHub/requests/', 'requests')
pycerfl.summary_Levels()