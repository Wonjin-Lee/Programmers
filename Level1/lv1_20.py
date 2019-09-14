def solution(s):
    answer = ''

    words = s.split(' ')

    for i in range(len(words)):
        temp = words[i]

        for j in range(len(temp)):
            if j % 2 == 0:
                answer += temp[j].upper()
            else:
                answer += temp[j].lower()
        
        if not i+1 == len(words):
            answer += ' '

    answer.rstrip()

    return answer

