#variable scoping
'''x=4 #global variable
def my_fun():
    global x #x is now a global variable
    x=3
    print(x)
my_fun()
print(x)'''

'''x=4 #global variable
def my_fun():
    x=3 #local variable
    print(x)
my_fun()
print(x)'''

'''var1=10 #global variable
def fun():
    var1=3 #non local variable
    print(var1)
    def fun2():
        var1=4 #local variable
        print(var1)
    print(var1)
    fun2()
fun()
print(var1)'''

'''var1=10 #global variable
def fun():
    var1=3 
    print(var1)
    def fun2():
        nonlocal var1
        var1=4 #nonlocal variable
        print(var1)
    print(var1)
    fun2()
fun()
print(var1)'''

