import itertools as it

def solution(nums):
    answer = 0

    li = list(map(list, it.combinations(nums, 3)))

    sosu_li = []

    for i in li:
        sosu_li.append(sum(i))

    for i in sosu_li:
        for j in range(2, i):
            check = True
            if i % j == 0:
                check = False
                break
        
        if check == True:
            answer += 1

    return answer

print(solution([1, 2, 7, 6, 4]))

'''
import itertools as it

def solution(nums):
    answer = 0

    for i in it.combinations(nums, 3):
        cand = sum(i)
        for j in range(2, cand):
            if cand % j == 0:
                break
        else:
            answer += 1
    return answer
'''