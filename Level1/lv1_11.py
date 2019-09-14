def solution(s):
    answer = True
    
    s = s.lower()
    if s.count('p') is 0 and s.count('y') is 0:
        return True

    if s.count('p') != s.count('y'):
        answer = False

    return answer

'''
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
'''