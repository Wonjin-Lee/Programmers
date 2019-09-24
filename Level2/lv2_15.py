import itertools

def solution(baseball):
    answer = 0

    allCase = list(map(list, itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)))

    print(len(allCase))

    for i in baseball:
        strike, ball, out = i[1], i[2], 3-i[1]-i[2]

        for j in allCase:
            comp_s, comp_b, comp_o = j
    
    return answer

base = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]

solution(base)