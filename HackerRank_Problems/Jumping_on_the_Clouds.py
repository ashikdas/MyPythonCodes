def jumpingOnClouds(c):
    jump = 0
    position = 0
    while position < len(c) - 1:
        if position + 2 >= len(c):
            position += 1
            jump += 1
        elif c[position + 2] == 0:
            position += 2
            jump += 1
        else:
            position += 1
            jump += 1
    return jump


result = jumpingOnClouds([0, 0, 0, 0, 1, 0])
print(result)
