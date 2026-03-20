import sys
input = sys.stdin.readline

N=int(input())
results=[]
for _ in range(N):
    a,b,c,d=map(int, input().split())
    if a==b and b==c and c==d:
        result=50000+(a*5000)
        results.append(result)
    elif a==b ==c or a==b==d or a==c==d:
        result=10000+(a*1000)
        results.append(result)
    elif b==c==d:
        result=10000+(b*1000)
        results.append(result)
    elif (a==b and c==d) or (a==c and b==d): #or (a==d and b==c):
        result=2000+(a*500) + (d*500)
        results.append(result)
    elif (a==d and b==c):
        result=2000+(a*500) + (b*500)
        results.append(result)
    elif (a==b) or (a==c) or (a==d):
        result=1000+(a*100) 
        results.append(result)
    elif (b==c) or (b==d):
        result=1000+(b*100) 
        results.append(result)
    elif (c==d):
        result=1000+(c*100) 
        results.append(result)        
                 
    else:
        x=[a,b,c,d]
        result = max(x)*100
        results.append(result)
            
print(max(results))       
        
             