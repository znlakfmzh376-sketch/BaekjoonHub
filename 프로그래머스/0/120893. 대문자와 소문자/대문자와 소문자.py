def solution(my_string):
    answer = ''
    for i in my_string:
        if i.islower()==1:
            answer += i.upper()
        else:
             answer += i.lower()
            
    return answer