import sys
input = sys.stdin.readline

N=int(input())

arr=list(map(int, input().split()))
arr2=set(arr)
arr2=list(arr2)
arr2.sort()
print(*arr2)