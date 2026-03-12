import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr1 = []

for i in range(len(arr)):
    
    if arr[i] == 1:
        arr1.append(arr[i])
        continue
    
    for j in range(2, int(arr[i]**0.5) + 1):
        if arr[i] % j == 0:
            arr1.append(arr[i])
            break

print(len(arr) - len(arr1))