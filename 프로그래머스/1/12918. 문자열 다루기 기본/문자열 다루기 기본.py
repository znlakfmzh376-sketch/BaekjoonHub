def solution(s):
    answer = True
    nums=['1','2','3','4','5','6','7','8','9','0']
    if (len(s)==4) or (len(s)==6):
        pass
    else:
        answer=False
    for i in s:
        if i not in nums:
            answer=False
    return answer