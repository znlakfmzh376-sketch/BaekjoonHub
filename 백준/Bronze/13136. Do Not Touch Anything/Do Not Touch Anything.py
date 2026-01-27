import sys

input=sys.stdin.readline

R,C,N= map(int,input().split())
if R%N==0:
    a=R//N
else:
    a=(R//N)+1 
if C%N==0:
    b=C//N
else:
    b=(C//N)+1
print(a*b)     
             