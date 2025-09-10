# A Module in python is basically a file with some Python code
# We use modules to organize our code into multiple files
# That each file is called a module and it should contain all the related functions and classes 

import converters   # We dont add the extension here --> Converters.py --> wrong --> only the file name  --> Converters --> right
                    # So now this 'converters' is an object
                
# instead of importing the entire module, we can import specific functions from the module
from converters import lbs_to_kg                                   # (ctrl + space buttons)

lbs_to_kg(100)
                    
print(converters.kg_to_lbs(70))