import sys
input = sys.stdin.readline

N=input().strip()
for i in range(len(N)):
    if i==0:
        print(N[i],end='') 
    elif i%10==0 :
        print('')
        print(N[i],end='')
         
         
    else:
        print(N[i],end='')
        
        
              
        