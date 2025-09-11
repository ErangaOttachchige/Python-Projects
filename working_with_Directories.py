from pathlib import Path     # pathlib — Object-oriented filesystem paths

# a path object to reference a file or directory on computer

# Absolute path  --> Eg: (C:\Users\\AppData\Local\Android)

# Relative Path --> a path stating from the current dirctory

path = Path("ecommerce") # this return a path object
print(path.exists())  # returns a boolean

# If we dont pass an argument here, this will reference the current directory
# Alternatively, we can pass string there, in this string we can add a file or a directory --> Path("ecommerce")

path2 = Path("emails")
# path2.mkdir()           # make a new directory
# path2.rmdir()             # remove a directory



# We can also find all the files and directories in a given path

path3 = Path()  # this will reference the current directory
for file in path3.glob('*.py'):    # with this method we can search for files and directories in the current path
  print(file)

# we can optinally add an extension
path3.glob('*.*')   # to get all the files with out directories in the current directory we use *.*
path3.glob('*.py')  # to get all the .py files in the current directory we use *.py
