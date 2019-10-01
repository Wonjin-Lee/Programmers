def solution(cookie):
    answer = 0

    for i in range(len(cookie)-1):
        for j in range(i, len(cookie)-1):
            leftSum = sum(cookie[i:j+1])
            for k in range(j+1, len(cookie)):
                rightSum = sum(cookie[j+1:k+1])
                if leftSum == rightSum and answer < leftSum:
                    answer = leftSum

    return answer

print(solution([1, 1, 2, 3, 1, 2, 1, 3]))