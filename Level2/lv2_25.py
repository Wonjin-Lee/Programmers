# Level 2 폰켓몬

def solution(nums):
    answer = 0

    pokemon_dic = [False for _ in range(200001)]

    for x in nums:
        pokemon_dic[x] = True

    pokemon_kind_num = pokemon_dic.count(True)

    if pokemon_kind_num >= len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = pokemon_kind_num

    return answer

print(solution([3, 3, 3, 3, 3, 3]))

'''
def solution(nums):
    return min(len(nums)/2, len(set(nums)))
'''