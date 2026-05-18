def solution(my_string):
    answer = 0
    temp = ''

    for i in range(len(my_string)):
        if my_string[i].isalpha():
            if len(temp) > 0:
                answer += int(temp)
                temp = ''
        else:
            temp += my_string[i]

    if temp:
        answer += int(temp)

    return answer