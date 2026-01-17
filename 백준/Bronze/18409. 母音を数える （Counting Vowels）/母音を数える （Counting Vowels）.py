import sys
input = sys.stdin.readline

N=int(input())
S=input().strip()
count=0
ch=['a','i','u','e','o']
for i in range(N):
        if S[i] in ch:
                count += 1
               
                 
print(count)         