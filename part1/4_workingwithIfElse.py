#Note: these programs should be run in the command line, not within Sublime Text's interpreter


#USING IF-ELSE STATEMENTS -- AND SOLICITING USER INPUT

# #If you've ever used the IF statements in Excel or a database manager like Access or MySQL, you're probably
# familiar with the concept of setting up a conditional argument. 
# If this is your first time exposed to it, it works like this:
#     - You think of something you want to be True or False
#     - If the relevant value is True, you tell Python to do one thing
#     - If it's False, you tell Python to do something else instead


# 1)

# A basic example: you're selling an item and won't take less than 100. 
# Let's write a program that screens potential buyers for you. If they offer less than
# 100, no deal. If they offer more than 100, deal.
# Note how we use "int" here to make sure the input is read as an integer.

if int(raw_input("How much can you offer? ")) < 100:
    print "Not enough"
else:
    print "You've got a deal!"


# 2)

# Here's another example... this time let's.
# TKTKTKTTKKTK


# 3)

# Here's another more sophisticated approach, using what's called a "flag":

# Let's say a bank has a promotion going to give you a free iPad if you 
# open an account and deposit more than $1,000.  
# If you don't put in $1,000, you won't get the iPad but instead a mug.
# There are several ways to write a Python program to deal with this - here is one...

# # First, we set up a variable that we want to use. The key trigger will be when the
# variable is True. Therefore, we need to set its default to actually be False.
freeipad = False

# Then, we put together our IF-ELSE statement, which will determine whether our variable is True or False
deposit = int(raw_input("How much do you want to deposit? "))
if deposit > 100 :
    freeipad = True #this part is the flag

# Now that we've set up the first conditional, we can write the part of the program that determines
# what the response will be, with another IF-ELSE statement
if freeipad :  #leaving this BLANK is the same as saying it's True. This essentially says if freeipad = True.
    print("You get a free iPad!")
else :
    print("Enjoy your mug.")

#Now let's say that no matter what gift the bank gives you, it still wants to wish you a nice day. To do that,
# we can place a print statement OUTSIDE the IF-ELSE statement at the bottom.
# This tells Python to give the response no matter the result of whether the variable is True or False.
print("Have a nice day.")



#Great, now we've got it. And here's how the language looks altogether:
freeipad = False
deposit = int(raw_input("How much do you want to deposit? "))
if deposit > 100 :
    freeipad = True #this part is the flag
if freeipad :  
    print("You get a free iPad!")
else :
    print("Enjoy your mug.")
print("Have a nice day.")


# 4)

# Now in addition to just IF-ELSE, you can actually have more than just two choices.
# To do that, you use ELIF - which stands for, you guessed, "Else If".

# Here's an example of how you'd set that up.
# Let's say you want to set up a program to ask people their favorite NFL football team.
# Since the Philadelphia Eagles are clearly the team to root for (despite many a disappointment to their fans of late),
# you want to celebrate the Eagles if someone chooses it.
# Now if they DON'T choose the Eagles, you want to give them a second chance to pick again.
# However - the Eagles can't stand the Dallas Cowboys, so if a person chooses the Cowboys, you want to stop
# right there and tell them where to get off.


chosenTeam=raw_input("What is your favorite football team? ")

if chosenTeam.upper() == "EAGLES" : #why do we uppercase this? To avoid case sensitivity in the answer
    print("Fly Eagles Fly!")
    print("E-A-G-L-E-S...Eagles!")
elif chosenTeam.upper() == "COWBOYS" :
    print("Go back to Texas. Seriously, just take your belt buckle and get out.")
else:
    print("You must like being a bum. The Eagles will crush that team.")
    print("Let's try this again.")
    secondTeam=raw_input("What is your favorite team? ")
    if secondTeam.upper() == "EAGLES" :
        print("Better believe it!")
        print("Fly Eagles Fly!")
    elif secondTeam.upper() == "COWBOYS" :
        print("Seriously? Take your belt buckle and get out of the here.")
    else:
        print("You're still a bum. Give it some thought and try again later.")

print("Have a nice day.")
