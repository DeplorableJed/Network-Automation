# Lab 2
# After each step save your script as "2.py" and run it in a virtual environment
# 1. Make a string variable with the Months of the year,
#    - Insert carriage returns after each month
#    - Print the variable to ensure the output is correct
# 2. Make a string variable that contains a short paragraph
#    - Indent the fisrt line with a tab
#    - Print the paragraph to the screen and verify output
# 3. Print the value between the stars *Jed's mom said "Hello World!"*
# 4. Have the scrip prmopt and collect the 4 following values:
#    - Your favorite color
#    - Your favorite food
#    - Your favorite drink
#    - Your favorite animal
# 5. Print these 4 variables to the screen
# Good Luck
months ="Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"
print (months)

paragraph = "\tBeautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let's do more of those!"
print (paragraph)

print ("Jed's mom said \"Hello World\"")

color = input("What is your favorite color?")
food = input("What is your favorite food?")
drink = input("What is your favorite drink?")
animal = input("What is your favorite animal?")

answers = "{} {} {} {}"
print (answers.format(color, food, drink, animal))
