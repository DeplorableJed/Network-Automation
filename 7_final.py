#This is your first Python Subscription
# After each step save your script as "6.py" and run it in a virtual environment
# 1. Import the datetime packate
# 2. define a function called print_time
#    - as part of the function print "task completed"
#    - still under the function use the following command *print(datetime.datetime.now())*
#    - still under the function print a blank line
# 6. Create a for loop that goes thru a range from 0-10
# 7. Call the function at the end to print the current time to the screen
# Good Luck
import datetime

def print_time():
    print('task completed')
    print(datetime.datetime.now())
    print()

for x in range(0,10):
    print(x)

print_time()
