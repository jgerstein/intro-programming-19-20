---
## Intro to Programming

#### Day 20 - Object Oriented Programming
---
## Do Now

What are some of the properties of a Pokemon? What are some of the things they can do? How might we create a Pokemon class?
---?code=day20/class1.py&lang=python

@[1](We are creating a class called `Cat`)
@[4, 14-16](`animal_type` is a *class variable*. It is the same for **all** cats and can be accessed for a specific cat or the generic Cat)
@[6-9](This is the constructor. We never call it directly, but it's called when we create an *instance* of the Cat class)
@[6, 8-9](`self` refers to the individual instance of the Cat class we're working with, so this takes in two arguments and assigns those values to the object-level variables)
@[11, 12](Creating two cats)
@[14-16](`animal_type` can be accessed by all cats and the generic Cat)
@[17-19](`name` and `age` are only accessible to the individual objects of the Cat class. Try running line 19)

---?code=day20/class2.py&lang=python

@[11-13, 23-24](The ony new thing here is the speak() method. What will it do? Could we modify it so they speak differently from each other)

---?code=day20/class3.py&lang=python

@[8-12](We have a new variable - `self.hunger`. How might we use it?)
@[18-23](We can create methods that modify the object's variables. This method decreases the cat's hunger level)
@[28-31](What will this do? How could we make a loop that continues to feed the cats until they're both done eating?)
---
## Pokemon

We'll try the Pokemon class together