def solution(number, k):
    answer = ''

    count = k

    numberList = list(map(int, number))

    startIdx = numberList.index(max(numberList[0:k+1]))

    del numberList[:startIdx]

    k -= startIdx

    for i in range(k):
        del numberList[numberList.index(min(numberList[:len(numberList)-k]))]

    answer = ''.join(list(map(str, numberList)))

    return answer