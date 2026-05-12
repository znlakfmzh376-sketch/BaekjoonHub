def solution(numbers):
    answer = 0
    arr=[]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i !=j:
                arr.append(numbers[i]*numbers[j])
    answer=max(arr)        
    return answer