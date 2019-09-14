def solution(n):
    
    temp = '수박'

    answer = ''

    if n % 2 == 0:
        answer = temp * (n // 2)
    else:
        answer = temp * (n // 2) + '수'

    return answer

'''
def solution(n):
    s = '수박' * n
    return s[:n]
'''

'''
def solution(n):
    return "수박" * (n // 2) + "수" * (n % 2)
'''