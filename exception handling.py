a=int(input("enter a number"))
b=int(input("enter b number"))
try:
    c=a/b
except:
    print("Error occured")
else:
    raise ZeroDivisionError("division is not possible")
   # print("a/b is ",c)
finally:
    print("Finally block executed")
