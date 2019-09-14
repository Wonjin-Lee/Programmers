def solution(answers):
    answer = []

    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]

    score = [0 for i in range(3)]

    for idx, result in enumerate(answers):
        if result == pattern1[idx % len(pattern1)]:
            score[0] += 1
        
        if result == pattern2[idx % len(pattern2)]:
            score[1] += 1

        if result == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, elem in enumerate(score):
        if elem == max(score):
            answer.append(idx+1)

    return answer