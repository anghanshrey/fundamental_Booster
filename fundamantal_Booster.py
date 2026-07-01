print("Welcome to the interactive Personal Data Collecter!")
print("")

name = input("Please enter your name:")
age = int(input("Please enter your age:"))
height = float(input("Please enter your height in meters:"))
number = int(input("Please enter your favourite number:"))
print("")

print("Thank you! Here is the information we collected:")
print("")

print(f"Name: {name} (Type:{type(name)}, Memory Address: {id(name)})")
print(f"Name: {age} (Type:{type(age)}, Memory Address: {id(age)})")
print(f"Name: {height} (Type:{type(height)}, Memory Address: {id(height)})")
print(f"Name: {number} (Type:{type(number)}, Memory Address: {id(number)})")
print("")

print(f"Your birth year is approximately: {2026-age} (based on your age of {age})")
print("")

print("Thank you for using the Personal Data Collector, Goodbye!")
