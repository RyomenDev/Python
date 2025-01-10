
a=10    # global variable if not defined in global - error
print('out a=',id(a))

def fun1():
    def some():
        # a=15    # local variable
        global a  # specify as global - can change value of a - no local variable more
        print('some before a=', id(a))
        a=15
        print('some after a=', id(a))
        print('in fun:',a)

    print('out-before-fun a=',id(a),a) #10
    some()
    print('out-after-fun a=',id(a),a) #15

# fun1()

# 

# global and local variable together
def fun2():
    def some2():
        a=9
        print('some2 a=', id(a))
        x=globals()['a']
        print('some x=', id(x))
        print('some2',a,x)
        globals()['a']=20 #will change value of ouside a without changing local
        print('some2 a=', id(a))

    some2()

    print('outside:',a)
    print('out a=',id(a))

fun2()