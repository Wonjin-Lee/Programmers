from collections import deque

def solution(s):
    answer = ''
    
    lower = []
    upper = []

    for i in range(len(s)):
        if s[i].islower():
            lower.append(s[i])
        elif s[i].isupper():
            upper.append(s[i])

    lower.sort()
    upper.sort()

    lower.reverse()
    upper.reverse()

    result = lower + upper
    answer = ''.join(result)

    return answer

'''
def solution(s):
    return ''.join(sorted(s, reverse=True))
'''