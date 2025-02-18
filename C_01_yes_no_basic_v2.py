
# functions go here

def yes_no(question):

    "Checks user response to question is yes / no (y/n), returns 'yes' or 'no'"""

    while True:

      response = input("do you want to see the instructions?" ).lower()

      # checks users enter yes / no / y / n
      if response == "yes" or response == "y":
           "yes"
      if response == "no" or response == "n":
           "no"
      else:
          print ("please enter yes or no")

# Main routine

#testing loop...
while True:

   want_instructions = yes_no("do you want to see the instructions? ")
   print (f"you chose {want_instructions}")

print("we done")