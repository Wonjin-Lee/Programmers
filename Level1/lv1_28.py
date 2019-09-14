def solution(x):

    copy = x
    li = []

    while True:
        if copy is 0:
            break

        li.append(copy % 10)

        copy = copy // 10
    
    if x % (sum(li)) == 0:
        return True
    else:
        return False

'''
def solution(n):
    return n % sum([int(i) for i in str(n)]) == 0
'''
