days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekday = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

def solution(a, b):
    answer = ''

    day_sum = 0

    for i in range(a-1):
        day_sum += days[i]
    
    day_sum += b

    answer = weekday[day_sum % 7]

    return answer

'''
def solution(a, b):
    answer = ''

    answer = weekday[(sum(days[:a-1]) + b) % 7]

    return answer
'''