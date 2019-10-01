# 레벨 2 위장
import itertools as it

def solution(clothes):
    answer = 1

    dic = {}

    for cloth in clothes:
        if dic.get(cloth[1]) == None:
            dic[cloth[1]] = 1
        else:
            dic[cloth[1]] += 1
    
    cloth_num = list(dic.values())

    for i in range(1, len(cloth_num)+1):
        temp = list(map(list, it.combinations(cloth_num, i)))
        print(temp)


    return answer

    #answer = map(lambda x: x * answer, cloth_num)

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["blue_sunglasses", "eyewear"], ["temp", "pants"], ["leoo", "pants"]])