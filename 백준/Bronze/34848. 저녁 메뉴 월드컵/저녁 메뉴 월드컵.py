import sys
input = sys.stdin.readline
T= int(input())
for i in range(T):
    a=int(input())
    count=0
    while a>1:
        if a%2 ==1:
            a=a//2 +1
            count +=1
        else:
            a=a//2    
    print(count)        
        
        
    

    
