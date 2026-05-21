def solution(dots):
    def is_parallel(a, b, c, d):
        dx1 = dots[b][0] - dots[a][0]
        dy1 = dots[b][1] - dots[a][1]
        dx2 = dots[d][0] - dots[c][0]
        dy2 = dots[d][1] - dots[c][1]
        
        return dy1 * dx2 == dy2 * dx1

    if is_parallel(0, 1, 2, 3):
        return 1
    if is_parallel(0, 2, 1, 3):
        return 1
    if is_parallel(0, 3, 1, 2):
        return 1
    
    return 0