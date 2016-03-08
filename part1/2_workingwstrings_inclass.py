# #STRINGS

# At its most basic, a string is just text - it can be displayed like this



# Let's create a variable assigned to a string instead.
# In Python, you don't have to declare a variable before you assign a value to it. 
# Just give it a name and assign it a value using the = sign.



#Once the variable is assigned, you can do all kinds of things with your string
#You can add other text to combine with it:


# .upper() is one of dozens of string method, in many ways similar to the functions you might be familiar with in Excel. 


# You might notice that the .upper() method doesn't permanently change the "variable" variable. 
# We'll get to that in a minute.


# You can also capitalize the first letter in the string


# Let's lowercase the string, too


#These work without variables at all, too, of course


# The built-in TYPE function tells us what type of Python object our "variable" is. 
# In this case, it's a string (or 'str'), which is a core type and brings with it a host of useful methods.



#SLICING AND DICING STRINGS

# You can use the brackets to 'slice' out characters from a string based on their position. 
# Notice in Python, that we start counting at zero. So variable[0] returns the "n" in "nicar". 
# The value after the colon is the position that we stop before. So variable[0:2] returns all the characters from 
# position 0 until before position 2.



#Using a variable of course works the same way


# Let's print the first four characters


# Let's print everything after the second character


# Remember when the .upper() method didn't change the variable? A string is immutable. 
# You can't change it in place, so if you want to change it, you have to create a NEW VARIABLE 
# and assign the new value to it.



#Another exmample - you can use replace() to do swap out part of the string for something new


#But look what happens when we call mystring...


# See what I mean? It doesn't "stick" unless you create a new variable


# Let's add the year to our string "pycar"


# Oops. You can't concatenate an integer and a string. Let's make that 16 a string by wrapping it in quotes.



#You can also use a function called SPLIT to split a string based on a certain character


# Let's try to split the string on the space


# Let's create a variable to hold this string


# Then let's get the type


# A list? Hmm. That's a new one.
# Because it's a list, we can again get a specfic item by it's index and we're back to where we started



#Wait, what IS a "list"???  
#Ask, and ye shall have an answer in the next step... --->>
