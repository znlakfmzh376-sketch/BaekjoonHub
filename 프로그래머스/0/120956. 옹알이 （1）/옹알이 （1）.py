def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        temp = b

        # 같은 발음이 두 번 나오면 불가능
        for word in words:
            if temp.count(word) > 1:
                break
        else:
            for word in words:
                temp = temp.replace(word, " ")

            if temp.strip() == "":
                answer += 1

    return answer