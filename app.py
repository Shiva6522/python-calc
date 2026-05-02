def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def divide(a,b):
    if b==0:
        raise ZeroDivisionError("Cannot Divide by 0")
    return a/b

a=int(input("Enter first Number: "))
b=int(input("Enter second Number: "))



while True:
    print("1.Add 2.Sub 3.Mul 4.Divide")
    ch=int(input("Enter choice: "))

    if ch==1:
        rs=add(a,b)
        print("Result: ",rs)
    elif ch==2:
        rs=sub(a,b)
        print("Result: ",rs)
    elif ch==3:
        rs=mul(a,b)
        print("Result: ",rs)
    elif ch==4:
        rs=divide(a,b)
        print("Result: ",rs)
    else:
        print("Exiting Bye..!!")
        break

