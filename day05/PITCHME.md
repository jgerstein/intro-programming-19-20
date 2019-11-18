---
## Intro to Programming

#### Day 5 - Data Types and Variabless
---
## Do Now

Exercise Day05:1 and Day05:2 in Repl.it classroom
---
## Core Concepts

* What is a variable?
* What are the main types of data?
* Formatting strings
---
# Variables
---
## Variable Basics

* Name representing some value
* Always lower case
* Join_words_with_underscores
---
## Assignment Statements

* Assign a vaolue to a variable
* Variable goes on left
* Value goes on right
* Single equal sign in middle
---
```python
a = 3
b = 2
c = a + b
print(c)
a = 5
print(c)
```
---
## Try It

Exercise Day05:3 will use this. Please complete and submit.
---
# Data Types
---
## String

* Text
* Always in quotes
* Examples: "Hello", 'Hi', '5', "Five"
---
## Integer

* Whole number
* Abbreviated as int
* Examples: 42, -3, 100, 0, 3
---
## Floating Point Number

* Decimal
* Abbreviated as float
* Examples: 1.0, 3.4, -5.2
---
## Boolean

* True or False
* Used for comparisons
---
## Try It

Exercise Day05:4 in Repl.it
---
# More Built-In Functions
---
## input()

* Input: Takes a prompt as an argument
* Process: Displays the prompt in console and waits for input
* Output: Returns user input to the program as a string
---
## input()

```python
my_name = input("Who are you? ")
print(my_name)
```
---
## str(), int(), float()

* Input: Takes a value to convert as an argument
* Process: Converts value to the specified type if possible
* Output: Returns value if converted successfully. Otherwise error.
---
## Conversions
    
```python
# Even if you respond with a number, my_num will be a string
my_num = input("Choose a number")
print(my_num * 5)
```
---
## Conversions

```python
# The user's input will be converted to a float
my_num = float(input("Choose a number"))
print(my_num * 5)
```
---
## Try It

Exercise Day05:6 in Repl.it
---
# Review
