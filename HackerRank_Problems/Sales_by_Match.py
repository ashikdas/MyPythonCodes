#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


# Complete the sockMerchant function below.

def sockMerchant(n, ar):
    pears = 0
    color = set()
    for i in range(len(ar)):
        if ar[i] not in color:
            color.add(ar[i])
        else:
            pears += 1
            color.remove(ar[i])
    return pears


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
