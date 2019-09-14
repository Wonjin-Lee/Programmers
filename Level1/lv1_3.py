def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        temp = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(temp[commands[i][2]-1])

    return answer

'''
def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command

        answer.append(list(sorted(array[i-1:j]))[k-1])

    return answer
'''