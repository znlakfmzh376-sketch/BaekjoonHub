import sys
input = sys.stdin.readline

N = int(input())
result = []
arr=list(map(int, input().split()))
for i in range(N):
    result.insert(len(result) - arr[i], i+1)
print(" ".join(map(str, result)))