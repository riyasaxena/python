# (shift 3 on windows lenovo to get hash)
# Write a program to print the traingle like this
# *
# **
# ***

# You can run your program located in learn/riya/python by giving the command python printPerpTriangle.py

# once you are done, issue these following commands so that I can see the code

# git add *
# git commit -m "I have done my program"
# git push
#
# Hint : To print a next line use a blank print() and to print on teh same line use someThing like print ("*",)
# You need to understand which command (instruction) is for outer loop and which one is for inner loop

# All the best
for loopdaloop in range(5) :
    print (loopdaloop)
    for inner in range(loopdaloop+1):
        print (inner)


for outer in range (3) : # 1 2
    for inner in range (outer + 1) :
        print ("outer = ", outer, " inner = ", inner)
        
for outer in range(1, 10):
    for inner in range (1, outer+1):
        print ("*", end="")
    print("")



for outer in range(10, 0, -1):
    for inner in range (1, outer+1):
        print ("*", end="")
    print("")

print("")

for outer in range(1, 6):
    for inner in range (0, (outer *2) -1):
        print ("*", end="")
    print("")



                                                                                                                             
# ***
# **
# *

# *
# ***
# *****
# *******
# *********