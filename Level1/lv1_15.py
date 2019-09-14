def solution(n):
    answer = 0

    numbers = [i for i in range(2, n+1)]

    for i in range(len(numbers)):
        if numbers[i] == 0:
            continue
        
        for j in range(2, numbers[i]+1):
            if i % j == 0:
                break
            if j == i-1:
                answer += 1

'''
def solution(n):
    num = set(range(2, n+1))
    
    for i in range(2, n+1):
        if i in num:
            num -= set(range(i*2, n+1, i))
    
    return len(num)
