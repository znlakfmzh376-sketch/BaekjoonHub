import sys
input = sys.stdin.readline
N= int(input())
vocas=[]
for i in range(N):
    vocas.append(input().strip())
vocas1=set(vocas) # 중복 제거
vocas=list(vocas1)
vocas.sort()
vocas.sort(key=len)
for v in vocas: 
    print(v)    