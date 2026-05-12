def solution(array):
    answer = 0
    arr=[]
    for i in array:
        arr.append(str(i))
    arr=''.join(arr)
    answer=arr.count("7")
    return answer