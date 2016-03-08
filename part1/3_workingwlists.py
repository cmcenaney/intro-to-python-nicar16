# #LISTS

# One of our favorite Python types is the list. 
# A list is an ordered collection of objects (variables, strings, integers, other lists, and more) 
# and is mutable. You create a list by assigning wrapping it in brackets and assigning it to a variable. 
# If you're familiar with JavaScript or Ruby, a Python list is very similar to an array.

mylist = ["Bob", "Sue", "Jim", "Renee"]

mylist

print mylist

# Because a list is a sequence (just as a string is a sequence of characters), we can also use the slicing method to pull out specific items from the list.

mylist[0:1]

mylist[3]


# A list can be CHANGED - with values added or swapped out 

# You add items to a list using the append() function

mylist.append("Cora")

print mylist

# Voila! Our list has now grown from four names to five

You can also change one of the names based on their index position, which we dealt with above. 

print mylist[3]

By using the index, we can change the value

mylist[3] = "Colleen"

#Now look what happens 

print mylist

# You can also delete items from a list using the DEL command

del mylist[2]

# It's also possible to combine lists together or replicate them

list2 = ["George", "Tony"]

print mylist + list2


#The same concepts work by using variables instead of a raw value

newname = "Tom"

mylist.append(newname)

print mylist


# PROMPTING USERS TO ENTER VALUES
# You can also prompt users to enter a value that you assign to a variable, 
# then use it to make lists
# (note: this code should be run in the command line)

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

for item in mylist:
    print item * 5




# For the final item, let's use the length of the list and lowercase the two strings we created to create a sentence
print 'I made %d strings from a list I created. They are: %s & %s' % (len(my_split_string), my_split_string[0].lower(), my_split_string[1].lower())


