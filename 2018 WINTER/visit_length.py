dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def solution(dirs):
    road = set()

    answer = 0

    x = 5
    y = 5

    for i in dirs:
        if i == "U":
            nx = x + dx[0]
            ny = y + dy[0]

        elif i == "D":
            nx = x + dx[1]
            ny = y + dy[1]

        elif i == "L":
            nx = x + dx[2]
            ny = y + dy[2]

        elif i == "R":
            nx = x + dx[3]
            ny = y + dy[3]
        
        if 0 <= nx and nx <= 10 and 0 <= ny and ny <= 10:
            road.add((x, y, nx, ny))
            road.add((nx, ny, x, y))
            x = nx
            y = ny

    answer = len(road) // 2

    return answer

print(solution("LULLLLLLU"))