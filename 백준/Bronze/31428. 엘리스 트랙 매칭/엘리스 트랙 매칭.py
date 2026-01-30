import sys
input = sys.stdin.readline

N=int(input())
A=input().strip()
b=input().strip()
count=0

for ch in A:
    if ch ==b:
        count+=1
print(count)        