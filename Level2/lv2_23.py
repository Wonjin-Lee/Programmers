# Level 2 다음 큰 숫자

def solution(n):
    answer = 0

    binary_n = str(bin(n))[2:]

    while True:
        n += 1
        
        if str(bin(n))[2:].count("1") == binary_n.count("1"):
            return n

print(solution(15))