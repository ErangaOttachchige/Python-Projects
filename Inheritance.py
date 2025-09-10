class Mammal:
  def walk(self):
    print("walk")


class Dog(Mammal): # this is how you inherit a class from a parent class, so our 'Dog' class inherits the 'walk' method from 'Mammal' class
  pass            # this basically means "nothing" more in this class

    
class Cat(Mammal):
  def be_annoying(self):
    print("annoying")


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.be_annoying()
cat1.walk()

# So both Dog and Cat classes are inheriting all the methods that we define in their parent class