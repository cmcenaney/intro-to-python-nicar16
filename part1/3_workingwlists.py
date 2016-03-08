# #LISTS

# One of our favorite Python types is the list. 
# A list is an ordered collection of objects (variables, strings, integers, other lists, and more) 
# and is mutable. You create a list by assigning wrapping it in brackets and assigning it to a variable. 

mylist = ["Bob", "Sue", "Jim", "Renee"]

mylist

print mylist

# Because a list is a sequence (just as a string is a sequence of characters), we can also use 
# the slicing method to pull out specific items from the list.

mylist[0:1]

mylist[3]


# A list can also be CHANGED - with values added or swapped out 
# You add items to a list using the append() function

mylist.append("Cora")

print mylist

# Voila! Our list has now grown from four names to five
# You can also change one of the names based on their index position, which we dealt with above. 

print mylist[3]

# By using the index, we can change the value

mylist[3] = "Colleen"

#Now look what happens 

print mylist

# You can also delete items from a list using the DEL command

del mylist[2]

# It's also possible to combine lists together or replicate them

list2 = ["George", "Tony"]

print mylist + list2


#The same concepts work by using variables instead of raw values

newname = "Tom"

mylist.append(newname)

print mylist


# PROMPTING USERS TO ENTER VALUES
# You can also prompt users to enter a value that you assign to a variable, 
# then use it to make lists
# (note: this code should be run as a .py file via the command line)

print('Enter the name of cat 1: ')
catName1 = raw_input()
print('Enter the name of cat 2: ')
catName2 = raw_input()

print('The cat names are: ')
print(catName1 + ' ' + catName2)

#Now we'll use the two user-defined values to create a list
catlist = [catName1, catName2]
print "Here's my new list: "
print catlist



#FOR LOOPS

# Probably the most powerful (and potentially dangerous) thing to do with a list is to iterate over it using a for loop, 
# to perform some action on each item in the list.

# Let's start with a list of numbers
# note that numbers don't have quotes (") around them

numlist = [1,2,3,4,5]
print numlist

# Now let's use a FOR LOOP to pull out each individual item in our list. 
# An important, though someone confusing aspect, is that the name you give to the "items" can be virtually anything.
# Below we've called it "item" but we could just as easily have called it "apple" or "elephant".
# It's best though to make it descriptive of what you're seeking so you can remember what it is you've done.

for item in numlist:
    print item 

# Now watch this -- instead of just returning each individual number, let's
# do some math on each one. 
# Multiply each number on our list by 5 and give us the result.

for item in numlist:
    print item*5 

# There are certain Python functions that create lists for you of certain types.
# For example, here is how you can easily make a list of sequential numbers based
# on their range.

range(10)
print range(10)

# You don't have to start with zero - you can set any two values to find numbers between them

range(22,45)
print range(22,45)

# If we want to save our list to actually use, we'll want to assign to a variable

myrange = range(22,45)
print myrange

# Now let's use a loop to print out each number in our range, which is a list

for item in myrange:
	print item

#The same concepts of LOOPS work for strings/text as well

teamlist = ["Cowboys", "Giants", "Patriots"]

for team in teamlist:    
    print team

# Now let's add on something truthful about these teams 

for team in teamlist:    
    print team + " Stink!"
