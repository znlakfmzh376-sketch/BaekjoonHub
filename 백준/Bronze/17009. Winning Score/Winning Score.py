import sys

input=sys.stdin.readline

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

result1=3*a +2*b+c
result2=3*d+2*e+f
if result1>result2:
    print("A")  
elif result1<result2:
    print("B")  
else:
    print("T")        