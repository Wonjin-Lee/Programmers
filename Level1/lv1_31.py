def solution(x, n):
    answer = []

    temp = x
    for i in range(n):
        answer.append(temp)
        temp += x

    return answer

'''
def solution(x, n):
    return [i * x + x for i in range(n)]
'''