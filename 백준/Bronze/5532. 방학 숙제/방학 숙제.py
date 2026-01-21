import sys
input = sys.stdin.readline

L=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())
result1=0
result2=0

if A%C==0:
    result1=int(A/C)
else:
    result1=A//C +1
if B%D==0:
    result2=int(B/D)
else:
    result2=B//D +1
if result1<result2:
    print(L-result2)
elif result1>result2:
    print(L-result1)
else:
    print(L-result1)                