def solution(skill, skill_trees):
    answer = 0

    for i in range(len(skill_trees)):
        skillQueue = list(skill)
        check = True
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skillQueue:
                if skill_trees[i][j] is not skillQueue[0]:
                    check = False
                    break
                elif skill_trees[i][j] is skillQueue[0]:
                    del skillQueue[0]
        
        if check == True:
            answer += 1

    return answer

'''
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
'''