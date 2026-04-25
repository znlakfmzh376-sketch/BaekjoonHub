import sys
input = sys.stdin.readline

n= int(input())
# 500,100,50,,10,5,1
change=1000- n
a=change // 500
b = (change%500) // 100
c = (change%500%100) // 50
d = (change%500%100%50) // 10
e = (change%500%100%50%10) // 5
f = (change%500%100%50%10%5) // 1
print(a+b+c+d+e+f)