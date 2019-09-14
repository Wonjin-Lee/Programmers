def solution(arr):
    arr.remove(min(arr))

    return arr

    if len(arr) == 0:
        return [-1]
    else:
        return arr

'''
def solution(arr):
    return [i for i in arr if i > min(arr)]
'''