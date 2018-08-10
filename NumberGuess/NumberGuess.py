"""
The program should do the following
- Roll a pair of dice
- Add the values of the roll
- Ask the user to guess a number
- Compare the user's guess to the total value
- Determine the winner (user or computer)
"""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess some number which can be the sum of rolled dices: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides * 2
  print "The max value can be %d" % (max_val)
  guess = get_user_guess()
  if guess > max_val:
    print "The guess is invalid, it cannot be greater than %d" % (max_val)
  else:
    print "Rolling . . ."
    sleep(2)
    print "First roll value is %d" % (first_roll)
    sleep(1)
    print "Second roll value is %d" % (second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print "Total of roll is %d" % (total_roll)
    print "Result . . ."
    sleep(1)
    if guess == total_roll:
      print "Hey Congratulations You WON!!!"
    else:
      print "We are Sorry but You Lose try next time"
      

roll_dice(6)