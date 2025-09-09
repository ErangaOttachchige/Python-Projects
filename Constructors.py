class Point:
  # Constructor --> A Constructor is a special method that gets called at the time of creating an object
  def __init__(self, x, y):  # Constructor  # self --> is a referance to the current object
    self.x = x               #  Here we are setting the attributes x and y for the object
    self.y = y               #  We use 'self' to referance the current object and then we can set attributes for that object using self
  
  
  def move(self):
    print("move")
    
  def draw(self):
    print("draw")
    
    
point = Point(10,20) # This 'point' object will have its x and y coordinates initialized
# point.x = 11
print(point.x)  # This will raise an AttributeError because 'Point' object has no attribute 'x'



# 2nd exercise

class Person:
  def __init__(self, name):     # Constructor with parameter 'name' 
    self.name = name            # setting the attribute 'name' for the object using self, we are setting the 'name' attribute of the current object to the value passed in the parameter 'name'
  
  # every method in the class should have this 'self' parameter and it should be the very first parameter of each method
  def talk(self):
    print(f"Hi, I am {self.name}")
  
  
john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()

# So each object is a differnt instance of a person class