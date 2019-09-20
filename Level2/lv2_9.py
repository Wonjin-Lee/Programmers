def solution(name):

    s = list(name)
    init = ["A"] * len(s)

    move_sum = 0
    shift_sum = 0
    idx = 0

    while True:
        move_right = 1
        move_left = 1

        up_alpha = ord(s[idx]) - ord("A")
        down_alpha = abs(ord(s[idx]) - ord("Z") - 1)

        shift_sum += min(up_alpha, down_alpha)
        s[idx] = "A"

        if s == init:
            break
        
        for i in range(len(s)):
            if s[idx + i] == "A":
                move_right += 1
            else:
                break
            if s[idx - i] == "A":
                move_left += 1
            else:
                break

        if move_left >= move_right:
            move_sum += move_right
            idx += move_right
        else:
            move_sum += move_left
            idx += move_left

    return move_sum + shift_sum