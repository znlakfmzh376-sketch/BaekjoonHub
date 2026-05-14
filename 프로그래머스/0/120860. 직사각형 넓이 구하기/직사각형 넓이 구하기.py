def solution(dots):
    answer = 0
    x=((dots[1][0]-dots[0][0])**2 +(dots[1][1]-dots[0][1])**2)**0.5
    y=((dots[2][0]-dots[0][0])**2 +(dots[2][1]-dots[0][1])**2)**0.5
    z=((dots[2][0]-dots[1][0])**2 +(dots[2][1]-dots[1][1])**2)**0.5
    s=[x,y,z]
    s=sorted(s)
    answer=s[0]*s[1]
    return answer