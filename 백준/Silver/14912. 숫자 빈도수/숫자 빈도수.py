import sys
input = sys.stdin.readline

n,d = map(int,input().split())
count =0
d=str(d)
for i in range(1,n+1,1):
    x=str(i)
    y=x.count(d)
    count +=y
print(count)    