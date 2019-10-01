def solution(strs, t):
    answer = 0

    strs.sort(key=len, reverse=True)

    print(strs)

    return answer

solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple")