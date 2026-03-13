import sys
input = sys.stdin.readline

while True:
    A,B=map(int,input().split())
    if A ==0 and B==0:
        break

    C=min(A,B)-abs(A-B)
    print(C)
    

    
