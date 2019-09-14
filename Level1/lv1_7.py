def solution(arr):
    answer = []

    cur = -1

    for i in range(len(arr)):
        if cur != arr[i]:
            answer.append(arr[i])
            cur = arr[i]

    return answer

'''
def solution(arr):

    return [s[i] for i in range(len(arr)) if s[i] != s[i+1:i+2]]
'''