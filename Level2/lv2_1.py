def solution(progresses, speeds):
    answer = []

    while len(progresses) != 0:

        if progresses[0] >= 100:
            cnt = 0
            while len(progresses) != 0 and progresses[0] >= 100:
                cnt += 1
                del progresses[0]
                del speeds[0]

            answer.append(cnt)

        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
    return answer

'''
def solution(progresses, speeds):
    daysLeft = list(map(lambda x: (ceil((100-progresses[x]) / speeds[x])) , range(len(progresses))))
    count = 1
    retList = []

    for i in range(len(daysLeft)):
        try:
            if daysLeft[i] < daysLeft[i+1]:
                retList.append(count)
                count = 1
            else:
                daysLeft[i+1] = daysLeft[i]
                count += 1
        catch:
            retList.append(count)
    
    return retList
'''
