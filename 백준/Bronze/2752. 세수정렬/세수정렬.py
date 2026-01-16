import sys
input = sys.stdin.readline
x,y,z=map(int,input().split())
a=[x,y,z]
a.sort()

for i in range(len(a)):
        print(a[i],end=" ")