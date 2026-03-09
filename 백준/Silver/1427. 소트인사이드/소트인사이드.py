import sys
input = sys.stdin.readline
N= input().rstrip()
result=[]
for i in range(0,len(N),1):
    result.append(N[i])
result.sort(reverse=True)
print(''.join(result))    