import sys
input=sys.stdin.readline
odd=[]
for i in range(7):
    a=int(input())
    if a%2 !=0:
        odd.append(a)
    else:
        continue
if len(odd)==0:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))            
 