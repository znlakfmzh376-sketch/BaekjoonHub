import sys
input = sys.stdin.readline

a,b=map(int, input().split())
if 2*a>=b:
    print("E")
else:
    print("H")    