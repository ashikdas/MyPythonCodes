from collections import Counter


def beautifulPairs(A, B):
    res = 0
    A = sorted(A)
    B = sorted(B)

    acnt = Counter(A)
    bcnt = Counter(B)

    spare = 0
    for el in acnt.items():
        if el[0] in bcnt:
            get = bcnt[el[0]]
            res += min(el[1], get)
        else:
            spare += el[1]

    print("res = {} spare = {}".format(res, spare))

    if spare:
        res += 1
    else:
        res -= 1

    return res


result = beautifulPairs([3, 5, 7, 11, 5, 8], [5, 17, 11, 10, 5, 8])
print(result)
