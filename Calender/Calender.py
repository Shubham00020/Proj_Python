"""
The program should behave in the following
= Print a welcome message to the user
= Prompt the iser to view, add, update, or delete an event on the calender
= Depending on the user's input: view, add, update, or delete an event on the calender
= The program should never terminate unless the user decides to exit
"""

from time import sleep, strftime

name = raw_input("Enter ur name: ")
calendar = {}
def welcome():
  print "Hii "+name+"! Welcome to the Command Line Calendar."
  print "Calendar is Openning . . ."
  sleep(1)
  print strftime("%A %B %d, %Y")
  print strftime("%I:%M:%S")
  print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Enter ur choice: \n A => Add \n U => Update \n V => View \n D => Delete \n X => Exit \n \t:").upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print "The Calendar is Empty"
      else:
        print calendar
    elif user_choice == 'U':
      date = raw_input("What date? (MM/DD/YYYY) ")
      if date in calendar.keys():
	      update = raw_input("Enter the update: ")
	      calendar[date] = update
	      print "The update is successfully made"
	      print calendar
      else:
        print "No event found for this Date"
    elif user_choice == 'A':
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print "An INVALID date was entered"
        try_again = raw_input("Try Again? Y for Yes, N for No: ").upper()
        if try_again == 'Y':
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "Event was successfully added"
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print "Calendar is Empty"
      else:
        event = raw_input("What event?")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "Event was successfully deleted"
            print calendar
            break
          else:
            print "An INCORRECT event was specified"
    elif user_choice == 'X':
      start = False
    else:
      print "INVALID command was entered"
      start = False
        
start_calendar()