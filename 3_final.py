#This is your first Python Subscription
# After each step save your script as "3.py" and run it in a virtual environment
# 1. Using input collect the following pieces of information
     - Your first name
     - Your family Name
     - Your age
     - Your country of residence
# 2. Using @operators print out the following sentence *<first name> <last name> is <age> years old and lives in <country>*
     - substitute the values you collected into the sentence dynamically
# 3. Use the .format function to print out the same sentence and variables dynamically
# 4. Use an f string to print out the same sentence and variables
# 5. Bonus change the first_name and last_name to upper case
# Good Luck

first_name = input("What is your first name?")
last_name = input("What is your last name?")
age = input("What is your age?")
age = int(age)
country = input("What is your country?")
print ("%s %s is %d years old and lives in %s"%(first_name, last_name, age, country))

print ("{} {} is {} years old and lives in {}".format(first_name, last_name, age, country))

print (f"{first_name} {last_name} is {age} years old and lives in {country}")

print (f"{first_name.upper()} {last_name.upper()} is {age} years old and lives in {country}")
