def solution(arr):
    answer = 0
    exit=0
    for i in range(len(arr)):
        if exit == 1:
            break
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                answer =0
                exit=1
                break
            else:
                answer = 1
    return answer
