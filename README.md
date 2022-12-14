# Analog Devices Coding Challenge
_This repository contains a solution for the below problem._

## Python Line Count Exercise
Write a Python program that takes a directory as a required argument and a filename extension as an optional argument that defaults to “.txt.” The program should locate all files with the given extension in the given directory and all its subdirectories to produce a list of all matching files with the number of lines within the file. The program should also output the total number of lines and the average number of lines per file. For example:
```
./file1.txt		10
./file2.txt		25
./d1/d1fa.txt	5
./d1/d1fb.txt	37
===============
Number of files found: 	4
Total number of lines:		77
Average lines per file:	19.25
```

## Solution

### Installation
No installation required

### Input 
It takes two arguments
1. Directory Name(mandatory). Example: ``` C://Users//VIJAYA//Desktop//test ```
2. File Extension(optional). Example: ```.txt ``` OR ``` .csv```

### How to run
```python line_count.py```

### Output
__Without extension or ```.txt```__ 

![Text extension](./images/text.PNG "Text extension")

***

__With ```.csv``` extension__

![Text extension](./images/csv.PNG "Text extension")





