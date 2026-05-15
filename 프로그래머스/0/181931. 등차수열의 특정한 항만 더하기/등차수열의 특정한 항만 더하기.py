def solution(a, d, included):
    answer = 0
    arr=[]
    for i in range(len(included)):
        b=a+(i*d)
        arr.append(b)
    for i in range(len(included)):
        if included[i]==1:
            answer += arr[i]
    
    return answer