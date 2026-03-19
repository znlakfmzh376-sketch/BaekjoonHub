import sys
input = sys.stdin.readline

results=[]
result=0
for i in range(4):
    a,b=map(int,input().split())
    add=b-a
    result += add
    results.append(result)
print(max(results))    
    
    

