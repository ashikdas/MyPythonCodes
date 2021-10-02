def solution(N):
    result = []
    for i in range(1, 11):
        val = N*i
        result.append(val)
    return result


N = int(input())
table = solution(N)
for j in range(0, len(table)):
    print(table[j], end=" ")