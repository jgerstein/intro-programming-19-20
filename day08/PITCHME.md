---
## Intro to Programming

#### Day 8: Loops
---
## Do Now

Exercise Day08:1
---
## Core Concepts

* Conditional statements
* Loops
---
## While Loops

* *while* something is True *do* something
* ideal for when you don't necessarily have a set of items or a set number of repetitions

```python
n = 0

while n <= 100:
    print(n)
    n += 1
```
---
## For loops

* *do* something *for each item* in a range

```python
for x in range(101):
    print(x)
```
---
```python
people = ["Jen", "Jean", "Jim", "Bill", "Rick", "Audrey", "Kung"]

for person in people:
    print(f"Good morning {person}")
```
---
## Iterables

* For loops require a series of some sort to iterate over
* Common types: list, range(), string
---
## range()

```
range(max)
range(min, max)
range(min, max, step)
```
* **input:** max, min/max, or min/max/step
* **process:** generate a range with the specified parameters
* **output:** range object
---
## string

Can loop through a string. Each letter will be a separate repetition
---
## list

* Will be covered in more detail soon
* Comma-separated values in square brackets
---
# Combining Everything
---
## Guess the secret number

We'll go through pseudocode and flowchart as a class
---
## Try It

Repl for the secret number program is published under projects.