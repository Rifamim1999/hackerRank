#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    count1= 0
    count2 = 0
    a = scores[0]
    for i in scores:
        if i>a:   #whenever there will be a grater score than score[0] then, it will count and will change the value of a.
            a = i
            count1+=1
    b = scores[0]
    for j in scores:     #whenever there will be a lower score than score[0] then, it will count and will change the value of b.
        if j<b:
            b = j
            count2+=1
    li = [count1, count2]
    return li

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
