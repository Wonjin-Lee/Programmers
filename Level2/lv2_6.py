def solution(n):
    answer = ''

    numberTable = {1 : "1", 2 : "2", 0 : "4"}

    mok = 1
    na = 1

    while mok != 0:
        mok = n // 3
        na = n % 3

        if na == 0:
            mok -= 1

        n = mok

        answer = numberTable[na] + answer

    return answer