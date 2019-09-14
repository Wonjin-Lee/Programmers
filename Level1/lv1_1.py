def solution(participant, completion):
    answer = ''
    check = True

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            check = False
            answer = participant[i]
            break

    if check == True:
        answer = participant.pop()

    return answer

'''
def solution(participant, completion):
    answer = ''
    
    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer.keys())[0]