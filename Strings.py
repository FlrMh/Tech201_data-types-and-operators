# Strings

# Single_quotes = 'Look! Single quotes.'
# Double_quotes = "Look! Double quotes."
#
# print(Single_quotes)
# print(Double_quotes)
#
# # Single quotes aren`t just used for quotes for strings! Single quotes are used in actual quotes.
#
# # string_failure = 'I sad 'Wow!'' # Python can`t tell where you want your string to end.
#
# # It`s better practice to just use double_quotes for strings
# # We can still use single_quotes
#
# escape_example = 'I said \'Wow!\''
# print(escape_example)
#
# quote_in_quote = 'I said "Wow"'
# print(quote_in_quote)
#
# reverse_quote = "I said 'Wow!' "
# print(reverse_quote)
# reverse_quote might be the best method to use quotes without creating confusion.



# # String slicing:
#
# # Everything in code starts with 0 not 1.
# # H e l l o   W o r l d  !
# # 0 1 2 3 4 5 6 7 8 9 10 11
# #         -6 -5 -4 -3 -2 -1
# Hw = "Hello world!"
# print(Hw[7:]) # orld! (when using Indexing, when specifying up until what point you want to slice the string, the idex that you specify as an ending point, will not be printed)
# print(Hw[7:9]) # or (prints from the first mentioned point up until the point before the ending point mentioned)
# print(Hw[-5:]) # orld! (counts back from the end of indexing)
# print(Hw[:5]) # Hello (counts from the beginning of indexing up until the 5th point)
# print(Hw[0:5]) # Hello (everything from the point 0 to point 5)
#
#
# # String methods (built-in)
#

# # Strip() - clears all the white space at the end of a string
# white_space = "lots of space at the end                                                   "
# print(len(white_space)) #75
# print(len(white_space.strip())) #24
#
#
# # A few more (showcasing them using the below string)
# example_text = "Here`s some text with lots of text"
#
# # Count a substring within a string - counting how many times a word occurs within a string
#
# print(example_text.count("text")) # 2
# print(example_text.count("t")) # 6
# print(example_text.count("Here`s some")) # 1
#
# # Make everything lower case
# print(example_text.lower())
#
# # Make everything upper case
# print(example_text.upper())
#
# # Capitalize things:
# print(example_text.capitalize())
#
# # Replace characters/text
# print(example_text.replace("with" , ",")) # the first "" contain the word we want to replace , after the comma, in the second "" we want to add what we want to replace it with
#

# # Concatenation (adding together multiple strings)
# a = "here "
# b = "more "
# c = "much more"
# print(a + b + c) # heremoremuch more
# print(a + " " + b + " " + c)
# # or you can add spaces at the end of your strings in order to make the end result readable


# # Casting
#
# # -Numeric to string
# x = 2
# y = 5.4
# z = " there`s a number 25.4 unless we put a space!"
# print(x + y + z) # will not work as we re adding numeric types with strings
# print(str(x) + "," + str(y) + z) # it works because we converted the numeric data into strings
#
# # -String to numeric
# int_string = "6"
#
# print(float(int_string))
# print(type(int(int_string)))


# F-strings (Formatted strings)

# name = "Lassie"
# years = 7
# height_cm = 60.2
#
# print(f"{name} is {years} years old and {height_cm} cm tall.") # using the f"{variable1} {variable2}...", Python formats the variables and will put together all the variables regardless of the data type they are


# F-strings allow us to use evaluations/methods too

# name = "Snoopy"
# years = 52
# print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS!!!")
#
# # You can use F-strings to specify precision in rounding and decimals
# pi = 3.14159265359
# print(f"Pi to 3 decimal places: {pi:.3f}") # Pi to 3 decimal places
# print(f"Pit to 5 decimal places: {pi:.5}") # Pi to 5 decimal places
#
# score = 16
# max_score = 26
# print(f"You scored {score/max_score}") # You scored 0.6153846153846154
# print(f"You scored {score/max_score:%}") # You scored 61.538462%
# print(f"You scored {score/max_score:.2%}") # You scored 61.54%
# print(f"You scored {score/max_score:.0%}") # You scored 62%






