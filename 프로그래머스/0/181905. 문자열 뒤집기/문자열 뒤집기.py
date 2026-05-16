def solution(my_string, s, e):
    c=len(my_string)
    answer = my_string[:s] +my_string[-(c-e):-(1+c-s):-1] +my_string[e+1:]
    return answer