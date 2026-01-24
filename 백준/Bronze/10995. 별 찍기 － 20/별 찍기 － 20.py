import sys
input = sys.stdin.readline

N=int(input())
for i in range(1,N+1,1):
    if i %2 !=0:
        for j in range(1,2*N,1):
            if j%2==0:
                print(" ",end="")
            else:
                print("*",end="")             
    else:
        print(" ",end="")
        for j in range(1,2*N,1):
            if j%2==0:
                print(" ",end="")
            else:
             print("*",end="")          
    
 
 
    print()   
