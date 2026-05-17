def solution(arr, queries):
    answer = []
    for i, j in queries:
        temp = 0
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
    return arr