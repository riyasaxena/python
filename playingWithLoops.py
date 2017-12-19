startRange = int (input("Enter the number from which you want to start printing tables: "))
endRange = int (input("Enter the number till which you want to print tables: "))

# 
for anumber in range (startRange, endRange) :
    print 
    print  "timestable of ", anumber     
    print
    for loopdaloop in range (1, 11) :
        print anumber, "*", loopdaloop, "=", anumber * loopdaloop
        
        
