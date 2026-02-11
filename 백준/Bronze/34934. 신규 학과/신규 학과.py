import sys
input = sys.stdin.readline

a=int(input())

for i in range(a):
    s=input().strip() 
    if '2026' in s:
        result=s
   
print(result[:-4])                  