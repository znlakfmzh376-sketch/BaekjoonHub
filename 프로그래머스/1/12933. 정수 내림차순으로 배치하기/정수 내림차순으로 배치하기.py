def solution(n):
    answer = 0
    arr=[]
    for i in str(n):
        arr.append(i)
    arr=sorted(arr,reverse=True)    
    answer=int("".join(arr))    
        
    return answer