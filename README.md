# ***Tech201-Data types and operators***
An introduction to Data types and operators in Python.



- In programming, **data type** is an important concept.

*Variables* can store data of different types, and **different types** can do **different things**.

Python has the following data types built-in by default, in these categories:
- Text Type:	`str`
- Numeric Types:	`int`, `float`, `complex`, `longs`
- Sequence Types:	`list`, `tuple`, `range`
- Mapping Type:	`dict`
- Set Types:	`set`, `frozenset`
- Boolean Type:	`bool`
- Binary Types:	`bytes`, `bytearray`, `memoryview`
- None Type:	`NoneType`

We are going to look at the main ones : `str`, numeric types (`int`, `float`), `booleans` and `None`.

## 1.Strings `str`

A **String** `str` in Python is a single character or a collection of characters. It is the data type used to store text.

- In Python, a string can be created by enclosing it with either single or double quotes. Best practice is to use *double quotes* to avoid confusion throughout the code.
- Single quotes are used in actual quotes, hence why using single quotes to create a string can lead to confusion and errors!
- !! If we insist on using single quotes, we can still use them, but in the following escape methods:
1. Escape Method:
```bash
escape_example = 'I said \'Wow!\' '
print(escape_example) # This will print "I said 'Wow'!" due to the use of "\\"
```
2. Quote-in-Quote
```bash
quote_in_quote = 'I said "Wow!"'
print(quote_in_quote)
```
**Reverse quote** is the best method to use in order to avoid confusion. 
```bash
reverse_quote = "I said 'Wow!' "
print(reverse_quote)
```
### String Methods (built-in)

1. String slicing:

Everything in code starts with 0 not 1.
```bash
H e l l o   W o r l d  !
0 1 2 3 4 5 6 7 8 9 10 11
.........-7-6-5-4-3 -2 -1
Hw = "Hello world!"
print(Hw[7:]) # orld! (when using Indexing, when specifying up until what point you want to slice the string, the idex that you specify as an ending point, will not be printed)
print(Hw[7:9]) # or (prints from the first mentioned point up until the point before the ending point mentioned)
print(Hw[-5:]) # orld! (counts back from the end of indexing)
print(Hw[:5]) # Hello (counts from the beginning of indexing up until the 5th point)
print(Hw[0:5]) # Hello (everything from the point 0 to point 5)
```
2. Strip() - clears all the white space at the end of a string
```bash
white_space = "lots of space at the end                                                   "
print(len(white_space)) #75
print(len(white_space.strip())) #24
```
#### A few more methods (showcasing them using the below string)

example_text = "Here`s some text with lots of text"
3. Count a substring within a string - counting how many times a word occurs within a string
```bash
print(example_text.count("text")) # 2
print(example_text.count("t")) # 6
print(example_text.count("Here`s some")) # 1
```
4. Make everything lower/upper case
```bash
print(example_text.lower())
print(example_text.upper())
```
5. Capitalize letters
```bash
print(example_text.capitalize())
```
6. Replace characters/text
```bash
print(example_text.replace("with" , ",")) # the first "" contain the word we want to replace , after the comma, in the second "" we want to add what we want to replace it with
```
7. Concatenation (adding together multiple strings)
```bash
a = "here "
b = "more "
c = "much more"
print(a + b + c) # heremoremuch more
print(a + " " + b + " " + c)
# or you can add spaces at the end of your strings in order to make the end result readable
```
8. Casting

a. Numeric to string
```bash
x = 2
y = 5.4
z = " there`s a number 25.4 unless we put a space!"
print(x + y + z) # will not work as we re adding numeric types with strings
print(str(x) + "," + str(y) + z) # it works because we converted the numeric data into strings
```
b. String to numeric
```bash
int_string = "6"
print(float(int_string))
print(type(int(int_string)))
```
9. F-strings (Formatted strings)
```bash
name = "Lassie"
years = 7
height_cm = 60.2
print(f"{name} is {years} years old and {height_cm} cm tall.") # using the f"{variable1} {variable2}...", Python formats the variables and will put together all the variables regardless of the data type they are
```
F-strings allow us to use evaluations/methods too
```bash
name = "Snoopy"
years = 52
print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS!!!")
```
You can use F-strings to specify precision in rounding and decimals
```bash
pi = 3.14159265359
print(f"Pi to 3 decimal places: {pi:.3f}") # Pi to 3 decimal places
print(f"Pit to 5 decimal places: {pi:.5}") # Pi to 5 decimal places

score = 16
max_score = 26
print(f"You scored {score/max_score}") # You scored 0.6153846153846154
print(f"You scored {score/max_score:%}") # You scored 61.538462%
print(f"You scored {score/max_score:.2%}") # You scored 61.54%
print(f"You scored {score/max_score:.0%}") # You scored 62%
```


## 2. Numeric Types `int`, `float`, `complex`

In Python, there are three distinct numeric types: **integers**, **floating point numbers**, and **complex numbers**. We will focus on `int` and `float`.

a. Integers or `int` is a whole number, **positive or negative**, **without decimals**, of **unlimited length**.

b. Floating point number or `float` is a number, **positive or negative**, containing **one or more decimals**.

These numeric data types are often used alongside operators:
Operators :
1. *Arithmetic operators* = numerical operations:
- Add `+`
- Substract `-`
- Miltuply `*` 
- Divide `/`
2. *Comparison operators*:
- Greater `>`
- Smaller `<` 
- Equal `==`
- Unequal `!=`
- Greater or equal `>=`
- Smaller or equal `<=` 



#### Implementing numeric types
1. Ints

```bash
a = 24
b = 16

print(a + b) # 40
print(a > b) # True
print(a < b) # False
```

2. Floats
- Floats and ints ca be added together; because they are numeric types, Python has no issue adding them together

``` bash
FloatNum = 1.356
IntNum = 4

print(FloatNum + IntNum) # 5.356

# There`s no limit to the size of the decimal in Python, but Python will round things up

one_third = 1 / 3
print(one_third)  # 0.33333333333

print(one_third * 3)  # 1.0 (because Python rounds it up when you do na operation to it)
```


## 3.Booleans `True` or `False` 

Python **boolean** type is one of the built-in data types provided by Python, which represents one of the two values i.e. **True** or **False**.
```bash
a = True
b = False
print(a == b) # False
print(a != b) # True
print(a >= b) # True(True is greater than false - Python recognizes True as greater than False)
print(a >= True) # True
print(b <= False) # True
```
```bash
print(True and False) # False(Python can only return it true if both sides are true)
print(False and True) # False
print(False or True) # True(Because true is an option, Python will return true)
```
- Booleans are very useful for *quick rechecking* the state of something and *making a decision* based on that state.
- The other area Booleans are really useful in are *validating data types*.

#### Booleans with Data types:

1. Strings
```bash
hi = "Hello world!"
print(hi.isalpha()) # False (not all the characters in the string are alphabet letters)
print(hi.islower()) # False (Capital H)
print(hi.isupper()) # False
print(hi.endswith("!")) # True
print(hi.startswith("Hello")) # True
```

2. Numeric types
```bash
x = 0
y = 10
print(bool(x)) # False (0 is always considered False)
print(bool(y)) # True
```

## 4.None `None`

Although known as Null in other programming languages, **None** is used to define a null value or Null object in Python. It is *not the same as an empty string*, *False*, or *zero*. It is a data type of the class *NoneType object*.

```bash
print(bool(None)) # False (for Python, None has a false value)
x = None
print(x == False) # False
print(x == True) # False
# Because None, True and False are independent. None is neither True nor false.
```
 Checking if a variable is None
```bash
print(x == None) # Direct comparison - in more complex situations it can become a problem
Instead:
print(x is None) # True (BEST PRACTICE)

print(type(x)) # <class 'NoneType'>
```
- Overall None is good for placeholders, but it is not used for much.

!!! WHEN USING TRUE/FALSE/NONE, YOU ALWAYS NEED TO CAPITALIZE THEM! OTHERWISE, THEY WILL NOT BE RECOGNISED.
