def solution(s):
    answer = ''
    s=sorted(s)
    for ch in s:
        if s.count(ch) == 1:
            answer += ch
    return answer