'''
# 최대 인원이 정해지지 않은 코드
def solution(people, limit):
    answer = 0

    boat = 0

    people.sort()

    while True:
        if len(people) == 0:
            break

        for i in range(len(people)-1, -1, -1):
            if (boat + people[i]) <= limit:
                boat += people[i]
                people.pop(i)
            else:
                break

        if boat == limit or len(people) == 0:
            boat = 0
            answer += 1
            continue

        prev_people_idx = 0
        max_value = 0
        while True:
            check = True
            for i in range(-1, len(people)-1):
                if boat + people[i+1] <= limit and people[i+1] >= people[prev_people_idx]:
                    max_value = people[i+1]
                    prev_people_idx = i
                elif i == -1:
                    check = False
                    break
                else:
                    boat += people[prev_people_idx]
                    people.pop(prev_people_idx)
                    break
            
            if check == False:
                answer += 1
                boat = 0
                break

    return answer

solution([70, 50, 80, 50], 100)
'''

def solution(people, limit):
    answer = 0

    people.sort()

    boat = 0

    left_idx = 0
    right_idx = len(people)-1
    while True:
        boat = 0
        if left_idx > right_idx:
            break

        boat += people[right_idx]

        if people[left_idx] + boat <= limit:
            left_idx += 1
            right_idx -= 1
        else:
            right_idx -= 1
        
        answer += 1

    return answer

'''
def solution(people, limit):
    people.sort()
    answer = 0

    first = 0
    last = len(people)-1

    while first < last:
        if people[first] + people[last] <= limit:
            first += 1
        
        last -= 1
        answer += 1

    if first == last:
        answer += 1

    return answer
'''