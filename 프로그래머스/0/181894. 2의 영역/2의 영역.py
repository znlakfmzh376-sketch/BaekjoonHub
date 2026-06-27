def solution(arr):
    answer=[]
    x=arr.count(2)
    if x ==0:
        answer.append(-1)
    else:
        start=arr.index(2)
        end =len(arr)-1-arr[::-1].index(2)
        for i in range(start,end+1):
            answer.append(arr[i])
            
    
    return answer