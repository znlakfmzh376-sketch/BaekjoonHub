import sys
input = sys.stdin.readline
N= int(input())
spot=[]
for i in range(N):
    x,y=map(int,input().split())
    spot.append((x,y))
spot.sort(key=lambda x:(x[0],x[1]))
for i in spot:
    print(i[0],i[1])
