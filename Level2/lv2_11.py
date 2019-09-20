import heapq as hp

def solution(scoville, K):
    answer = 0

    hp.heapify(scoville)

    while True:
        first = hp.heappop(scoville)
        if first >= K:
            break

        if len(scoville) == 0:
            return -1

        second = hp.heappop(scoville)

        hp.heappush(scoville, first + second * 2)
        answer += 1

    return answer

    
scoville = [1, 2, 3, 9, 10, 12]
print(solution(scoville, 7))