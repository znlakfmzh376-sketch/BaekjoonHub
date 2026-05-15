def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        a=parts[i][0]
        b=parts[i][1]
        answer += my_strings[i][a:b+1]
    return answer