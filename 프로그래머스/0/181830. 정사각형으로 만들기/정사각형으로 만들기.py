def solution(arr):
    answer = [[]]
    x=len(arr)
    y= len(arr[0])
    if x== y:
        answer=arr
    elif x>y:
        for i in range(x):
            for _ in range((x-y)):
                arr[i].append(0)
        answer=arr
    else:
        temp=[0]*y
        for i in range(y-x):
            arr.append(temp)
        answer=arr    
            
    return answer