def solution(s):
    answer = ''

    leng = len(s)

    if leng % 2 == 0:
        answer = s[int((leng/2)-1):(int(leng/2)+1)]
    elif leng % 2 == 1:
        answer = s[int(leng/2)]

    return answer