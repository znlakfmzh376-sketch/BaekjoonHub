def solution(n):
    answer = [[0] * n for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y, d = 0, 0, 0
    num = 0

    for i in range(n * n):
        num += 1
        answer[x][y] = num

        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]

        x = nx
        y = ny

    return answer