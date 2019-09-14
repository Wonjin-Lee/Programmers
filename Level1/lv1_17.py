def solution(s):
    answer = 0

    if s[0].isdigit():
        answer = int(s)
    else:
        if s[0] == '-':
            answer = int(s[1:]) * -1
        elif s[0] == '+':
            answer = int(s[1:])

    return answer

print(solution('1234'))

'''
def solution(s):
    answer = int(s)
    return answer
'''