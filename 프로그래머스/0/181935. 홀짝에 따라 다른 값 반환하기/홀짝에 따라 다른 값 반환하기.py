def solution(n):
    result=0
    if n %2 !=0:
        for i in range(1,n+1,2):
            result += i
        answer=result    
    else:
        for i in range(2,n+1,2):
            result += i**2
            
        answer=result    
    return answer
print(solution(7))
print(solution(10))
