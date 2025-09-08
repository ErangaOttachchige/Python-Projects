# Dictionaries --> key value pairs

customer = {
  "name": "John Smith",
  "age": 30,
  "is_verified": True
}

print(customer["name"])
print(customer["age"])

print(customer.get("birthdate"))
print(customer.get("birthdate", "Jan 1 1980"))

# Exercise

phone = input("Phone: ")
digits_mapping = {
  "1": "One",
  "2": "Two",
  "3": "Three",
  "4": "Four",
  "5": "Five"
}

output = ""

for character in phone:
  output += digits_mapping.get(character, "!") + " "
   
print(output)
  