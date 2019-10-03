'''
def solution(s):
    box = []

    for st in s:
        if st == "(":
            box.append("(")
        else:
            if len(box) == 0:
                return False
            else:
                if box.pop() == ")":
                    return False

    if len(box) != 0:
        return False
    else:
        return True

print(solution("(())()"))
'''

def solution(s):
    box = []

    for st in s:
        if st == "(":
            box.append(st)
        elif st == ")":
            try:
                box.pop()
            except IndexError:
                return False

    return len(box) == 0

print(solution("(())()"))