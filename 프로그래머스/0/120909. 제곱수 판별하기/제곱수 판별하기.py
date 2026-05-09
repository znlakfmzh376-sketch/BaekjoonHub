def solution(n):
    result = int(n**0.5) 
    if result**2==n:
        answer=1
    else:
        answer=2
    return answer