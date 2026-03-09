import sys
input = sys.stdin.readline
N= int(input())
human=[]
for i in range(N):
    x,y=input().split()
    x=int(x)
    human.append((x,y))
human.sort(key=lambda x: x[0])
for i in human:
    print(i[0],i[1])