# Write a program to print times table of 2

print "2 * 1 = 2"
print "2 * 2 = 4"
print "2 * 3 = 6"


# its too boring and difficult to change... whats the point of using a computer
#ridiculous

#lets ask computer to so some work for us

# but how

# we want to use the calculator power of computer

print "2 * 1 = ", 2*1
print "2 * 2 = ", 2*2
print "2 * 3 = ", 2*3

# ahhh now the problem is.. its too lengthy

# Therefore... I can see that its a repeating pattern (ahhh loop) and everytime I increment the mulitplier with 1

# here comes the for loop
for anumber in range (1, 10):
    # print 2 * anumber
    print "2 * ", anumber, " times = ", 2 * anumber


# this is cool

# what if I want to change the number... rather provide a number

# print "For which number you want to print a table "

# inputNumber = input()

inputNumber = input("For which number you want to print a table : ")

for loopdaloop in range (1, 11) :
    print inputNumber,"*",loopdaloop, "times =" ,inputNumber * loopdaloop