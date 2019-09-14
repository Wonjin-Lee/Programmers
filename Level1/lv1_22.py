def solution(n):

    answer = list(str(n))

    result = list(map(int, answer))

    result.reverse()

    return result

'''
def solution(n):
    return list(map(int, reversed(str(n))))
'''