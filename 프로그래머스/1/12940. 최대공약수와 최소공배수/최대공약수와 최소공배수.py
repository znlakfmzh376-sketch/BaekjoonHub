import math
def solution(n, m):
    a=math.gcd(n,m)
    b=math.lcm(n,m)
    answer = [a,b]
    return answer