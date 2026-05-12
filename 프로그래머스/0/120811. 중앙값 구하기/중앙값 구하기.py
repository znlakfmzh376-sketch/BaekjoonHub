def solution(array):
    x=len(array)
    y=int(x/2)
    array=sorted(array)
    answer = array[y]
    return answer