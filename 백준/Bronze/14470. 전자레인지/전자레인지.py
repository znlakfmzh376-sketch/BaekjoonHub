import sys
input = sys.stdin.readline

A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())

if A<0:
    A=abs(A)
    temp=(A*C)+D+(E*B)
    print(temp)
elif A>0:
    print((B-A)*E)    
