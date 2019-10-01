'''
def solution(s):
    answer = 0

    idx = 0
    while True:
        if len(s) == 0:
            answer = 1
            break
        
        if len(s)-1 == idx:
            break

        if s[idx] == s[idx+1]:
            s = s[:idx] + s[idx+2:]
            idx = 0
        else:
            idx += 1

    return answer

st = "abbacc"

print(solution(st))
'''
'''
def solution(s):
    stack = []

    top = -1

    s = list(s)

    if len(s) % 2 != 0:
        return 0

    while True:
        if len(stack) == 0 or stack[top] != s[0]:
            stack.append(s.pop(0))
            top += 1
        elif stack[top] == s[0]:
            stack.pop(top)
            top -= 1
            s.pop(0)

        if len(s) == 0:
            break

    if len(stack) == 0:
        return 1
    else:
        return 0

print(solution("aadcde"))
'''
def solution(s):
    answer = []

    for i in s:
        if len(answer) == 0:
            answer.append(i)
        else:
            if answer[-1] == i:
                answer.pop()
            else:
                answer.append(i)
    
    if len(answer) == 0:
        return 1
    else:
        return 0