def solution(arr):
    answer = []
    x=len(arr)
    target=1
    while target<x:
        target *=2
    for i in range(target-x):
        arr.append(0)
    return arr