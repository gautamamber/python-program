import math
run=True
while run:
    print(" 1.  Addition")
    print(" 2.  Subtraction")
    print(" 3.  Division")
    print(" 4.  Multiplication")
    print(" 5.  Square of a no")
    print(" 6.  Cube of a no")
    print(" 7.  Square root of a no")
    print(" 8.  Factorial of a no")
    print(" 9.  Log10")
    print(" 10. cos")
    print(" 11. sin")
    print(" 12. tan")
    print(" 13. Exit")
    print(" enter your choice")
    choice=int(input())
    if choice==1:
        print("Enter the two values")
        a=int(input())
        b=int(input())
        c=a+b
        print(c)
        print("------------------------------------------------------------------------------------------------")
    elif choice==2:
        print("Enter the two values")
        a=int(input())
        b=int(input())
        c=a-b
        print(c)
        print("------------------------------------------------------------------------------------------------")
    elif choice==3:
        print("Enter the two values")
        a=int(input())
        b=int(input())
        c=a*b
        print(c)
        print("------------------------------------------------------------")
    elif choice==4:
        print("Enter the two values")
        a=int(input())
        b=int(input())
        c=a/b
        print(c)
        print("------------------------------------------------------------")
    elif choice==5:
        print("Enter a no")
        a=int(input())
        c=a*a
        print(c)
        print("------------------------------------------------------------")
    elif choice==6:
        print("Enter a no")
        a=int(input())
        c=a*a*a
        print(c)
        print("------------------------------------------------------------")
    elif choice==7:
        print("Enter a no")
        a=int(input())
        c=math.sqrt(a)
        print(c)
        print("----------------------------------------------------------- ")
    elif choice==8:
        print("Enter a no")
        a=int(input())
        c=math.factorial(a)
        print(c)
        print("-----------------------------------------------------------")
    elif choice==9:
        print("Enter a no")
        a=int(input())
        c=math.log10(a)
        print(c)
        print("-----------------------------------------------------------")
    elif choice==10:
        print("Enter an angle")
        a=int(input())
        c=math.cos(a)
        print(c)
        print("-----------------------------------------------------------")
    elif choice==11:
        print("Enter an angle")
        a=int(input())
        c=math.sin(a)
        print(c)
        print("-----------------------------------------------------------")
    elif choice==12:  
        print("Enter an angle")
        a=int(input())
        c=math.tan(a)
        print(c)
        print("-----------------------------------------------------------")
    elif choice==13:
        run= False
    else:
        print("Invalid choice")
    
