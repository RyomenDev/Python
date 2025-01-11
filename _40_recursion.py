
import sys
print(sys.getrecursionlimit())  #1000

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())  #set limit to 2000


def greet(i):
    print('hello',i)
    i=i+1
    greet(i)

i=1
# greet(i)  # by default limit 1000

def fact(n):
    if(n==0 or n==1):
        return 1;
    return n*fact(n-1);

print(fact(4));