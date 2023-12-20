#types of functions
'''def my_funct(*args): #positional dynamic arguments
    for i in args: #args- name of tuple in which arguments are stored
        print(i)
my_funct("hello",3,4,5,[1,2,3])'''

'''def my_function(age,name): #keyword based arguments
    print(age)
    print(name)
my_function(name="hello",age=13)''' 

'''def my_function(name,age):
    print(name)
    print(age)
my_function("hello",13) #positional arguments'''

'''def suma(*args): #program to demonstrate function to calculate sum and average of numbers given by user using dynamic argument passing positional arguments
    sum=0
    for i in args:
        sum+=i
        print(i,end=' ')
    print(sum,end='')
    avg=sum/len(args)
    print(avg)
suma(5*3+4,1,2)'''
'''n=int(input("Enter a number(0 to exit): "))
while n!=0:
    sum(n)
    n=int(input("Enter a number(0 to exit): "))'''

'''def myfunction(*args):  #program to calculate sum of numbers using dynamic positional argument passing
    tsum=0
    for i in args:
        #print(i,end=' ')
        for j in i:
            print(j,end=' ')
            tsum+=j
    print("\nSum:",tsum)
a=[]
n=int(input("Enter a number(0 to exit): "))
while n!=0:
    a.append(n)
    n=int(input("Enter a number(0 to exit): "))
print(a)
myfunction(a)'''

'''def my_fun(a,*args):
    print("a:",a)
    print("args:",args)
my_fun(a=1,2,3,4)'''

'''def my_function(**kwargs): #keyword based dynamic argument passing
    for i in kwargs: #kwargs- dictionary of keyword arguments with name,age as key and "abc" and 12 as values
        print(i,"=",kwargs[i])
my_function(name="abc",age=12)

def kbfunction(*args, **kwargs): #function that accepts positional and keyword based arguments
    print(args)
    print(kwargs)
    for i in args:
        print(i)
    for i in kwargs:
        print(i,"=",kwargs[i])
kbfunction("hello","ITM",name="abc",age=32)'''

'''def welcome(): 
    n=input("What is your name?\n")
    print("Welcome",n,"to ITM")
welcome()'''

'''def welcome(**kwargs):
    print("\nWelcome to ITM")
    for i in kwargs:
        print(i,"=",kwargs[i])
print("Enter your details:")
a=input("Name: ")
b=int(input("Age: "))
c=input("Email: ")
welcome(name=a,age=b,email=c)'''

'''import random
x=[]
def hello(**kwargs): #arbitrary arguments program
    print("\nYour details are:")
    c=random.randint(1,100)
    while c in x:
        c=random.randint(0,101)
    print("Roll number =",c)
    x.append(c)
    for i in kwargs:
        print(i,"=",kwargs[i])
a=int(input("Select what information you want to fill:\n1.Name\n2.Name and Age\n3.Name and Email\n4.Name, Age and Email\n"))
if a==1:
    b=input("Name:")
    hello(name=b)
elif a==2:
    b=input("Name:")  
    e=int(input("Age: "))  
    hello(name=b, age=e)
elif a==3:
    b=input("Name:")
    d=input("Email: ")
    hello(name=b, email=d)
elif a==4:
    b=input("Name:")
    e=int(input("Age: "))
    d=input("Email: ")
    hello(name=b,age=e, email=d)
else:
    print("Invalid choice")'''
