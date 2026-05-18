def solution(my_string):
    answer = ''
    arr =[]
    for i in range(len(my_string)):
        if my_string[i] in arr:
            pass
        else:
            answer += my_string[i]
            arr.append(my_string[i])
        
    return answer