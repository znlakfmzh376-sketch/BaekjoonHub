import sys
input = sys.stdin.readline

N,M=map(int,input().split())
if M==1 or M==2:
    print("NEWBIE!")
else:
    if N>=M:
        print("OLDBIE!")  
    else:
        print("TLE!")    

