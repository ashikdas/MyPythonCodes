#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 0
    if not any(i.isdigit() for i in password):
        count += 1
    if not any(i.islower() for i in password):
        count += 1
    if not any(i.isupper() for i in password):
        count += 1
    if not any(i in '!@#$%^&*()-+' for i in password):
        count += 1
    return max(count, 6 - n)


n = int(input().strip())

password = input()

result = minimumNumber(n, password)
print(result)

