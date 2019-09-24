def solution(citations):
    max = 0
    for i in range(1, len(citations)+1):
        

        cita_up = 0
        cita_down = 0

        for j in range(len(citations)):
            if citations[j] >= i:
                cita_up += 1
                continue
            
            if citations[j] <= i:
                cita_down += 1
        
        if cita_up >= i and cita_down <= i:
            max = i
    
    return max