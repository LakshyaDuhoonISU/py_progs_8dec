#arithmetic operations using functions
def add(a,b):
    print("Addition of",a,"and",b,"is",a+b)
def sub(a,b):
    print("Subtraction of",a,"and",b,"is",a-b)
def multi(a,b):
    print("Multiplication of",a,"and",b,"is",a*b)
def div(a,b):
    if b==0:
        print("Division is not possible")
    else:
        print("Division of",a,"and",b,"is",a/b)
def mod(a,b):
    print("Modulus of",a,"and",b,"is",a%b)
def floor(a,b):
    print("Floor division of",a,"and",b,"is",a//b)
def power(a,b):
    print(a,"^",b,"is",a**b)
def switch(c,d):
    a=int(input("Enter your choice\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Floor Division\n7.Power\n"))
    if a==1:
        add(c,d)
    elif a==2:
        sub(c,d)
    elif a==3:
        multi(c,d)
    elif a==4:
        div(c,d)
    elif a==5:
        mod(c,d)
    elif a==6:
        floor(c,d)
    elif a==7:
        power(c,d)
    else:
        print("Invalid choice")
c=float(input("Enter a number: "))
d=float(input("Enter another number: "))
switch(c,d)

'''def square(a):
    print(a,"^2 is",a**2)
def root(a):
    print("Root of",a,"is",a**0.5)'''
