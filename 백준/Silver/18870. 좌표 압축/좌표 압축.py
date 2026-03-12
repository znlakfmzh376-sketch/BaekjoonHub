import sys
import math
input = sys.stdin.readline

N=int(input())
nums=list(map(int,input().split()))

# 중복 제거
result1=set(nums)
arr=list(result1)

# 정렬해서 좌표 압축
arr.sort()
dic={}
for i in range(len(arr)):
    dic[arr[i]]=i

for n in nums:
    print(dic[n], end=" ")


