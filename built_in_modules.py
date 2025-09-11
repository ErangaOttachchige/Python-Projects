# built in Modules in python
# Python comes with a standard library that contains several modules for common tasks such as sending mails, working with date and time, generating random values and so on
import random  # we use this module to generate random values


for i in range(3):  
  print(random.random())           # generate a random value between 0 to 1
  print(random.randint(10, 20))                 # Return random integer in range [a, b], including both end points.
  
  
# Randomly picking an item from a list
members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)


# Roll a dice Exercise
class Dice:
  def roll(self):
    first = random.randint(1,6)
    second = random.randint(1,6)
    #return (first, second)   # when you want to return a tuple form a function, you dont have to add paranthesis explicity
    return first, second      # you can simplify your code and python will automatically iterpret this as a tuple
  


dice = Dice()
print(dice.roll())