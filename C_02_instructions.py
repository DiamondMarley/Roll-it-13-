
# functions go here

def yes_no():

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
def instructions():
    """Prints instructions"""

    print("""
"""  """"

Roll the dice and try to win! 
    """)
    

# Main routine

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no()

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
   instructions()

print()
print("Program continues")