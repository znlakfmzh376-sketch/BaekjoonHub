import sys
input = sys.stdin.readline

N=int(input())
angry=list(map(int,input().split()))
result=0
for i in range(N):
    if angry[i] == 1:
        result +=1
        angry[i]=result    
    elif angry[i] == 0:
        result -=1
        angry[i]=result   
        
print(sum(angry))
