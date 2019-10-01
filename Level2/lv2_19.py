def solution(numbers, target):
    answer = recursion(numbers, target, 0, 0)

    return answer

def recursion(numbers, target, idx, total):
    answer = 0

    if idx == len(numbers):
        if total == target:
            return 1
        else:
            return 0

    answer += recursion(numbers, target, idx+1, total + (-1 * numbers[idx]))
    answer += recursion(numbers, target, idx+1, total + numbers[idx])

    return answer

print(solution([1, 1, 1, 1, 1], 3))