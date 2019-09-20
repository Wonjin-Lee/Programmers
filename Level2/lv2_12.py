import itertools

def solution(numbers):
    
    li = []
    answer = 0

    for i in range(1, len(numbers)+1):
        li += list(map(int, set(map(''.join, itertools.permutations(list(numbers), i)))))

    li = set(li)

    maxi = max(li)

    idx = 0
    while True:
        if li[idx] 
            li -= set(range(i*2, maxi, i))

    li = list(li)

    print(li)

solution("032")