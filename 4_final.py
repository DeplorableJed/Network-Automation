#This is your first Python Subscription
# After each step save your script as "1.py" and run it in a virtual environment
# 1. Import argv from the sys package
# 2. Define 4 values to pass with argv (script, fruit, color, quantity)
# 3. Print the following using f strings *The script called <script> passed <quantity> <fruit> that are <color>
# Good Luck

from sys import argv

script,fruit,quantity,color = argv

print(f"The script called {script} passed {quantity} {fruit} that are {color}")
