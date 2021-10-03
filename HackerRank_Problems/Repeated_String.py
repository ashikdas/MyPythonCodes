def repeatedString(s, n):
    count_a_in_s = s.count('a')
    multiplier_of_s = n // len(s)
    remainder_of_s = n % len(s)
    count = multiplier_of_s * count_a_in_s + (s[0:remainder_of_s]).count('a')

    return count


st = repeatedString('abc', 100)
print(st)
