def solution(strArr):
    answer = 0
    arr = [0]*31
    for i in strArr:
        a=len(i)
        arr[a] +=1
    answer =max(arr)    
    return answer