import sys
input = sys.stdin.readline

N,L=map(int,input().split())
h=list(map(int,input().split()))

h=sorted(h)
for i in h:
    if L>=i:
        L +=1
    else:
        break   
print(L)        