# .read(), .readline(), .readlines(), .readable()

employee_file = open(r"C:\Users\Eranga Ottachchige\Desktop\Python Basics Mosh\Python-Projects\Reading and writing files\employees.txt", "r")

print(employee_file.readable())
# print(employee_file.read())

# print(employee_file.readline())
# print(employee_file.readline())

# print(employee_file.readlines())  # Puth them inisde in a list[]

# print(employee_file.readlines()[2])


for employee in employee_file.readlines():   # this creates a list of employees in the .txt file
  print(employee)

employee_file.close()