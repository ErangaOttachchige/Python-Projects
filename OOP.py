# We use Classes to define new types
# These types can have methods that we define in the body of the Class
# And they can also have attributes that we can set anywhere in our programs

class Point:
  def move(self):
    print("move")
    
  def draw(self):
    print("draw")
    
    
# So with this class we defined a new type, so with this new type we can create new objects
# an object is an instance of a class
# Class simply define the blueprint or the template for creating objects and objects are the actual instances based on that blueprint

# to create an object type out the name of the class, and then call it like a function --> this creates a new object and then returns it
# So we can save that object in a variable
point1 = Point()
point1.draw()

# Apart from methods, these objects can also have attributes and these attributes are like variables that belong to a particular object
point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point() # this object is completely diffrent from the first object
point2.x = 1
print(point2.x)

# So each object is a different instance of a Point Class