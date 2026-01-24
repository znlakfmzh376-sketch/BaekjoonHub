import sys
input = sys.stdin.readline


a=int(input())
b=int(input())
result=b-a+24
if result>=24:
    print(result-24)
else:
    print(result)    