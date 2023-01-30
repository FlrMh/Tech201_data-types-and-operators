# Booleans


# True or False

# a = True
# b = False
# print(a == b) # False
# print(a != b) # True
# print(a >= b) # True(True is greater than false - Python recognizes True as greater than False)
# print(a >= True) # True
# print(b <= False) # True

# print(True and False) # False(Python can only return it true if both sides are true)
# print(False and True) # False
# print(False or True) # True(Because true is an option, Python will return true)

# Booleans are very useful for quick rechecking the state of something and making a decision based on that state.
# The other area Booleans are really useful in are validating data types.


# Booleans with Data types

# # 1. Strings
# # hi = "Hello world!"
# print(hi.isalpha()) # False (not all the characters in the string are alphabet letters)
# print(hi.islower()) # False (Capital H)
# print(hi.isupper()) # False
# print(hi.endswith("!")) # True
# print(hi.startswith("Hello")) # True


# 2. Numeric types
# x = 0
# y = 10
# print(bool(x)) # False (0 is always considered False)
# print(bool(y)) # True
# print(bool(z)) # True


# # None
#
# # None == null in a lot of other languages
# print(bool(None)) # False (for Python, None has a false value)
# x = None
# print(x == False) # False
# print(x == True) # False
# # Because None, True and False are independent. None is neither True nor false.
#
# # Checking if a variable is None
#
# print(x == None) # Direct comparison - in more complex situations it can become a problem
# # Instead:
# print(x is None) # True (BEST PRACTICE)
#
#
# print(type(x)) # <class 'NoneType'>
# # Overall None is good for placeholders, but it is not used for much.

# WHEN USING TRUE/FALSE/NONE, YOU ALWAYS NEED TO CAPITALIZE THEM! OTHERWISE, THEY WILL NOT BE RECOGNISED.


