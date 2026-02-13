import sys
input=sys.stdin.readline

N,K = map(int,input().split())
nums=[]

for i in range(1,N+1,1):
    if N%i==0:
        nums.append(i)
    else:
        continue
if K<=len(nums):
    print(nums[K-1])
else:
    print(0)            

