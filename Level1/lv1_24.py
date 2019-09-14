import math

def solution(n):
    answer = 0

    sqr = math.sqrt(n)

    if int(sqr) != sqr:
        return -1
    else:
        answer = (int(sqr) + 1) ** 2
    
    return answer

'''
def solution(n):

    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'
'''