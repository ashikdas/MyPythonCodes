def matchingStrings(strings, queries):
    count = 0
    result = []

    for i in range(0, len(queries)):
        temp = queries[i]
        for j in range(0, len(strings)):
            if temp == strings[j]:
                count += 1

        result.append(count)
        count = 0

    return result


print(matchingStrings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab']))
