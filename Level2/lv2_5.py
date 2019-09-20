def solution(bridge_length, weight, truck_weights):
    answer = 1

    bridgeQ = []
    timeCount = []

    while len(bridgeQ) != 0 or len(truck_weights) != 0:
        answer += 1

        if len(truck_weights) != 0 and sum(bridgeQ) + truck_weights[0] <= weight:
            bridgeQ.append(truck_weights[0])
            timeCount.append(bridge_length)
            del truck_weights[0]
    
        for i in range(len(timeCount)):
            timeCount[i] -= 1

        if timeCount[0] == 0:
            del bridgeQ[0]
            del timeCount[0]
        
    return answer