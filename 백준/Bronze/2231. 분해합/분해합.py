import sys
input = sys.stdin.readline

N=int(input())
results =[]

for i in range(1,N+1):
    result=i
    s= str(result)
    for j in range(len(s)):
        result +=int(s[j])
    if result==N:
        results.append(i)
   
if results:              
    print(min(results)) 
else:
    print(0)       