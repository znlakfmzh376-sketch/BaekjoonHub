import sys

input=sys.stdin.readline

n= int(input())
if n%2==1:
    for i in range(1,2*n+1,1):
        if n==1:
            print("*")
            break
        else:
            for j in range(n):
                if (i+j)%2==0:
                    print(" ",end="")
                else:
                    print("*",end="")
            print()        
#짝수                    
else:
    for i in range(1,2*n+1,1):
        if i%2==0:
            print(" ",end="")
        for j in range(1,n+1,1):
            if j%2==0:
                print(" ",end="")
            else:    
                print("*",end="")
        print()               

                   


# 짝수

                   


# 짝수
