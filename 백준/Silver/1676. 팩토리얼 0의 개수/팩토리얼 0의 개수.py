import sys
input = sys.stdin.readline

N=int(input())
result=1
count=0
for i in range(1,N+1,1):
    result = result * i
    

while True:
    if result %10 == 0:
        count +=1
        result= result // 10
        
    else:
        break
        
print(count)        
       
    