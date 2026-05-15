import math
def solution(num_list):
    answer = 0
    a = math.prod(num_list)
    b = sum(num_list) ** 2
    if a<b:
        answer=1
    else:
        answer=0
    return answer