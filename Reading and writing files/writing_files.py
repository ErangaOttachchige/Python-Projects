employee_file = open(r"C:\Users\Eranga Ottachchige\Desktop\Python Basics Mosh\Python-Projects\Reading and writing files\employees.txt", "w")

employee_file.write("Toby - Human Resources")
employee_file.write("\nkelly - Customer Service")

employee_file.close()

employee_file1 = open(r"C:\Users\Eranga Ottachchige\Desktop\Python Basics Mosh\Python-Projects\Reading and writing files\employees11.txt", "w")
employee_file1.write("kelly - Customer Service")
employee_file1.close()

HTML_file = open(r"C:\Users\Eranga Ottachchige\Desktop\Python Basics Mosh\Python-Projects\Reading and writing files\index.html", "w")
HTML_file.write("<p>This is HTML</p>")
HTML_file.close()