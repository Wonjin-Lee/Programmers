def solution(s):
    answer = True

    if len(s) is not 4 and len(s) is not 6:
        return False

    if not s.isdigit():
        return False

    return answer

'''
def solution(s):
    return s.isdigit() and len(s) in (4, 6)
'''