import sys
input = sys.stdin.readline

N=int(input())

for i in range(1,N+1,1):
    a=input()
    print(f"{i}. {a}",end="")    