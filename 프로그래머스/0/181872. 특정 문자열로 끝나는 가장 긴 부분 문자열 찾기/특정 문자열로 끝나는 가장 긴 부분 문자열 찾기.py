def solution(myString, pat):
    a = myString.rindex(pat)
    answer = myString[:a+len(pat)]
    return answer