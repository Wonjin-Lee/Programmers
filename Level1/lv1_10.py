def solution(strings, n):
    answer = []
    dic = {}

    for i in range(len(strings)):
        dic[i] = strings[i][n:]

    hey = dic.items()

    answer = sorted(hey)

    print(dic)
    print(hey)

strings = ['sun', 'bed', 'car']

solution(strings, 1)

'''
def solution(strings, n):
    answer = sorted(sorted(strings), key=lambda x : x[n])

    return answer
'''