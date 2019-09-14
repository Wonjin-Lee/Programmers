def solution(n, lost, reserve):
    answer = 0
    
    for i in range(len(lost)):
        if reserve.index(lost[i]-1) >= 0:
            lost.remove(lost[i])
            reserve.remove(lost[i]-1)
        else if reserve.index(lost[i]+1) >= 0:
            lost.remove(lost[i])
            reserve.remove(lost[i]+1)
    
    answer = n - len(lost)

    return answer

'''
def solution(n, lost, reserve):
    answer = 0

    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for r in _reserve:
        front = r-1
        back = r+1

        if front in _lost:
            _lost.remove(front)
        else if back in _lost:
            _lost.remove(back)
        
    answer = n - len(_lost)
    return answer
'''