def solution(a, b):
    answer = 0

    maximum = int()
    minimum = int()

    if a > b:
        maximum = a
        minimum = b
    elif a < b:
        maximum = b
        minimum = a
    else:
        answer = a
        return answer
    
    for i in range(maximum - minimum + 1):
        answer += minimum + i

    return answer

'''
def solution(a, b):
    if a > b:
        a, b = b, a
    
    return sum(range(a, b+1))
'''