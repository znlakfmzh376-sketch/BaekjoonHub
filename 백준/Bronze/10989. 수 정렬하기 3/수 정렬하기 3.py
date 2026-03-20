import sys
input = sys.stdin.readline

N=int(input())
count=[0]*10001

for i in range(N):
    a=int(input())
    count[a] +=1
    
for i in range(10001):
    for j in range(count[i]):
        print(i)    
    