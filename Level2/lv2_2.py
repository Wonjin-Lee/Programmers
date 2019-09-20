def solution(priorities, location):
    answer = 0

    retList = []

    indexList = [x for x in range(len(priorities))]

    while not len(priorities) == 0:
        if priorities[0] >= max(priorities):
            retList.append(indexList[0])
            del priorities[0]
            del indexList[0]
        else:
            priorities.append(priorities[0])
            indexList.append(indexList[0])
            del priorities[0]
            del indexList[0]

    answer = retList.index(location) + 1

    return answer