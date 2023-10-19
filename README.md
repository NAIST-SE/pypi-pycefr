# **pycefrl**
## *Identifying Python3 Code Level Using the CERFL Framework as Inspiration*

### What is this project about?
The goal of pycefrl is to create a tool capable of obtaining an evaluation inspired by the [''Common European Framework of Reference for Languages''](https://en.wikipedia.org/wiki/Common_European_Framework_of_Reference_for_Languages) for code written in the Python programming language, version 3.

With this tool it is possible to analyze the level of GitHub repositories (and their developers) or code snippets in Python3.

### ABSTRACT
Python is known to be a versatile language, well suited both for beginners and advanced users. Some elements of the language are easier to understand than others: some are found in any kind of code, while some others are used only by experienced programmers. The use of these elements lead to different ways to code, depending on the experience with the language and the knowledge of its elements, the general programming competence and programming skills, etc. In this paper, we present pycefr, a tool that detects the use of the different elements of the Python language, effectively measuring the level of Python proficiency required to comprehend and deal with a fragment of Python code. Following the well-known Common European Framework of Reference for Languages (CEFR), widely used for natural languages, pycefr categorizes Python code in six levels, depending on the proficiency required to create and understand it. We also discuss different use cases for pycefr: identifying code snippets that can be understood by developers with a certain proficiency, labeling code examples in online resources such as Stackoverflow and GitHub to suit them to a certain level of competency, helping in the onboarding process of new developers in Open Source Software projects, etc

### Usage
1. Prepare the files as follows
```text
Root folder of your project
└───projects
|   ├───sample directory
|
└───jupyter notebook
└───results
```

Current API 
```python
from pycefr import pycerfl

pycerfl.read_Directory('projects/sample directory', 'sample directory')
```
It should create a results folder with two files
- d.csv
- d.json

## Citation
If you use pycefr in your research or wish to refer to the examples in this repo, please cite with:

```bibtex
@inproceedings{RoblesICPC22,
author = {Robles, Gregorio and Kula, Raula Gaikovina and Ragkhitwetsagul, Chaiyong and Sakulniwat, Tattiya and Matsumoto, Kenichi and Gonzalez-Barahona, Jesus M.},
title = {Pycefr: Python Competency Level through Code Analysis},
year = {2022},
isbn = {9781450392983},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3524610.3527878},
doi = {10.1145/3524610.3527878},
booktitle = {Proceedings of the 30th IEEE/ACM International Conference on Program Comprehension},
pages = {173–177},
numpages = {5},
location = {Virtual Event},
series = {ICPC '22}
}
