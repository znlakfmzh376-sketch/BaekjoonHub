import sys
input = sys.stdin.readline

x,y = map(int,input().split())

def rev(x):
    return int(str(x)[::-1])

result=rev(x) + rev(y)
print(rev(result))