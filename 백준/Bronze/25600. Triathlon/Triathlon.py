import sys
input = sys.stdin.readline

N=int(input())
high_score=0
for i in range(N):
    a,d,g=map(int,input().split())
    if a==(d+g):
        score=(d+g)*2*a
    else:
        score=(d+g)*a    
    if  score>high_score:
        high_score=score
    else:
        continue
print(high_score)           