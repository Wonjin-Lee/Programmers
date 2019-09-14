def solution(n, m):
    answer = []

    mini = min(n, m)
    while True:
        if n % mini == 0 and m % mini == 0:
            answer.append(mini)
            break
        else:
            mini -= 1

    answer.append(int(answer[0] * (n / answer[0]) * (m / answer[0])))

    return answer

'''
def solution(n, m):
    c, d = max(n, m), min(n, m)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    
    answer = [c, int(a*b/c)]
    
    return answer
'''
