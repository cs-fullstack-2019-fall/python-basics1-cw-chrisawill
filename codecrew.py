# ## Problem 1:
# Create two variables. One should equal “My name is: “ and the other should equal your actual name. Print the two variables in one print message.
ask = "My name is "
myName = "Christian"
print (ask + myName)



# ### Problem 2:
# Ask the user to enter the extra credit they earned. If they entered less than 5 print “That’s not enough extra credit.” If they entered more than 20 print “That’s too much extra credit”.

credit = int(input("Enter your extra credit"))

if credit < 5:
    print("That's not enough extra credit.")
elif credit > 20:
    print("That's too much extra credit.")



# ### Problem 3:
# Ask a user to enter a password. Enter a password. Ask user to reenter password. Check to see if they are correct.

userPassword = input("Enter a password. ")
reEnter = input("Re-enter password. ")

if userPassword == reEnter:
    print ("Your password is correct")
elif userPassword != reEnter:
    print ("Incorect password. Try again.")









# ### Problem 4:
# Ask for two card numbers. If it equals 21 print BLACKJACK!, if it’s greater than 21 print BUST!, if it’s less than 21 print “The total is [THE TOTAL]”
#
card1 = int(input("Enter a card number"))
card2 = int(input("Enter a second card"))
total = card1+card2
if total < 21:
    print ("The total is " + total)
elif total == 21:
    print ("BLACKJACK!")
elif total > 21:
    print ("BUST!")