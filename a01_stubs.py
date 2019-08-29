######################################################################
# Author: Thy H. Nguyen      TODO: Change this to your name
# Username: nguyent2         TODO: Change this to your username
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year
from time import sleep
print()
print ("Do you want to know more about yourself? ")
thyhnguyen = int(input( "If yes, can you tell me when were you born? [Your year of birth needs to be between 2000 and 2011] "))
sleep(3)
# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples
print()
thy = ["Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit"]
if thyhnguyen == 2000:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[0],".")
elif thyhnguyen == 2001:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[1],".")
elif thyhnguyen == 2002:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[2],".")
elif thyhnguyen == 2003:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[3],".")
elif thyhnguyen == 2004:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[4],".")
elif thyhnguyen == 2005:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[5],".")
elif thyhnguyen == 2006:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[6],".")
elif thyhnguyen == 2007:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[7],".")
elif thyhnguyen == 2008:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[8],".")
elif thyhnguyen == 2009:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[9],".")
elif thyhnguyen == 2010:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[10],".")
elif thyhnguyen == 2011:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[11],".")
else:
    print("Can you please enter the birth year between 2000 and 2011? \n Re-enter your birth year to see the surprise!")
######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year
print()
print ("Now, you have known your Chinese Zodiac animal. What about your friends? \n Are you curious about your friend's Chinese Zodiac animal?")
birth_year = (input("What is your friend's year of birth? [Make sure that you remember to enter a year between 2000 and 2011] "))
print()
yearr = int(birth_year[-2:])
if yearr == 00:
    print ("Your friend's Chinese Zodiac animal is a Dragon.")
elif yearr == 1:
    print ("Your friend's Chinese Zodiac animal is a Snake.")
elif yearr == 2:
    print("Your friend's Chinese Zodiac animal is a Horse.")
elif yearr == 3:
    print("Your friend's Chinese Zodiac animal is a Goat.")
elif yearr == 4:
    print("Your friend's Chinese Zodiac animal is a Monkey.")
elif yearr == 5:
    print("Your friend's Chinese Zodiac animal is a Rooster.")
elif yearr == 6:
    print("Your friend's Chinese Zodiac animal is a Dog.")
elif yearr == 7:
    print("Your friend's Chinese Zodiac animal is a Pig.")
elif yearr == 8:
    print("Your friend's Chinese Zodiac animal is a Rat.")
elif yearr == 9:
    print("Your friend's Chinese Zodiac animal is a Ox.")
elif yearr == 10:
    print("Your friend's Chinese Zodiac animal is a Tiger.")
elif yearr == 11:
    print("Your friend's Chinese Zodiac animal is a Rabbit.")
else:
    print("Did you remember to enter a birth year between 2000 and 2011? \n Please try again!")

    # TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
