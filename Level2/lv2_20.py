import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    heap = []
    idx = 0
    while stock < k:
        for i in range(idx, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(heap, -supplies[i])
                idx += 1
            else:
                break
        
        stock += -heapq.heappop(heap)
        answer += 1

    return answer