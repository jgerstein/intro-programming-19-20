---
## Intro to Programming

#### Day 11 - Functions
---
## Core Concepts

* Functions
---
## Anatomy of a Function

```python
def function_name(argument):
    """This is a docstring and should always be included"""
    print("This is a simple function that just prints something")
    return
```
@[1](This line gives the function its name and define the arguments it will take)
@[2-4](The block of code will run when the function is called)
@[2](The docstring describes the function)
@[3-4](This is what the function does)
@[4](The function will exit even if you leave out return)
---
## How it works

```python
def star(sz):
    """Draw a star"""
    for x in range(5):
        t.fd(sz)
        t.rt(144)
    return


star(50)
```
@[9](Python gets to this line and starts looking for a definition of star())
@[1](Python finds the *first* place star() is defined and uses it)
@[1, 9](The argument given in the *function call* is assigned as the value for the parameter in the function definition)
@[3-6](The block of code is executed with `sz` having the value specified in the function call)
---
# Arguments
---
## Positional Arguments

* We've only looked at positional arguments so far
* Assigned in order they appear
* Every argument must be assigned a value

```python
def speak(cat_sound, dog_sound):
    """Print cat and dog sounds"""
    print(f"A cat says {cat_sound}")
    print(f"A dog says {dog_sound}")
    return

speak('meow', 'woof')
speak('woof', 'meow')
```
---
## Optional Arguments

* Assigning a value for an argument with a default will overwrite it
* Arguments with defaults can be excluded
* Must come after arguments without defaults

```python
def star(sz=100):
    """Draw a star"""
    for x in range(5):
        t.fd(sz)
        t.rt(144)
    return


star(50)
star()
```
---
## Keyword Arguments

* Every argument has a variable name
* Can assign to specific variable

```python
def repeated_pattern(reps, sz=100, ang=150, direction="right"):
    """Draw a repeated pattern. sz defaults to 100 and ang defaults to 150"""
    for x in range(reps):
        t.fd(sz)
        if direction == "left":
            t.lt(ang)
        else:
            t.rt(ang)
    return

repeated_pattern(10)
repeated_pattern(10, direction='left')
repeated_pattern(3, ang=120)
repeated_pattern(3, 150, 120, 'left')
```
@[11-14](All of these are valid ways to call the function. What would each do?)
---
# Output
---
## Return

* Every function returns something
* Some return `None`, others return a specific value
* Return a value by putting it after `return` in the function definition
* A returned value is made available to the main program
---
## Return

```python
def sum_1(a, b):
    """Find the sum of a and b"""
    result = a + b
    return

def sum_2(a, b):
    """Find the sum of a and b"""
    result = a + b
    return result

print(sum_1(3, 5))
print(sum_2(3, 5))
```

What will happen?