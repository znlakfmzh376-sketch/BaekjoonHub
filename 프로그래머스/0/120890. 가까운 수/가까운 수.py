def solution(array, n):
    answer = 0
    arr=[]
    temp=10000
    for i in array:
        x=abs(n-i)
        if x<temp:
            temp=x
        else:
            pass
    for i in array: 
        if temp == abs(n-i):
            arr.append(i)
    answer=min(arr)        
    return answer