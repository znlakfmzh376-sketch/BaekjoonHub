def solution(str1, str2):
    answer = str1.find(str2)
    if answer>=0:
        answer=1
    else:
        answer=2
    return answer