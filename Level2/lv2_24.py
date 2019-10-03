def solution(land):
    recursion(land, 0, -1, 0)
    global maximum
    answer = maximum
    return answer

def recursion(land, idx, prev, total):

    if idx == len(land):
        global maximum
        maximum = max(maximum, total)
        return

    for i in range(4):
        if prev != i:
            recursion(land, idx+1, i, total+land[idx][i])

maximum = 0
lan = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1], [100, 0, 9, 8]]

print(solution(lan))