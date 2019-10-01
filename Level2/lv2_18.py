import math

def solution(brown, red):
    answer = []
    cache = []

    if red == 1:
        answer.append(3)
        answer.append(3)
        return answer

    for i in range(1, int(math.sqrt(red))+1):
        if red % i == 0:
            cache.append([i, red // i])
    
    for x in cache:
        height = x[0]
        width = x[1]

        area = (width * 2) + ((height + 2) * 2)

        if area == brown:
            answer.append(width + 2)
            answer.append(height + 2)
            break

    return answer

print(solution(10, 2))

'''
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2 * (i + red // i) == brown - 4:
                return [red // i + 2, i + 2]
'''