def solution(phone_book):
    answer = True

    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i == j:
                continue
            if phone_book[j].startswith(phone_book[i]):
                answer = False
                return answer

    return answer