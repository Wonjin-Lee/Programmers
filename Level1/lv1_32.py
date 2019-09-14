def solution(d, budget):
    answer = 0

    d.sort()

    for i in range(len(d)):
        if d[i] > budget:
            break
        else:
            answer += 1
            budget -= d[i]

    return answer

'''
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    
    return len(d)
'''