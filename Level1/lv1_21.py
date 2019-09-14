def solution(n):
    answer = 0

    while True:
        
        if n == 0:
            break
        
        answer += n % 10
        
        n = n // 10

    return answer

'''
def solution(n):
    if n < 10:
        return n
    
    return (n % 10) + solution(n // 10)
'''

'''
def solution(n):
    return sum([int(i) for i in str(n)])
'''