#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    candles.sort(reverse = True)    #first i have sorted the list in decending order. so the highest number will be at index 0.
    count = 0
    for i in range(len(candles)):
        if candles[i] == candles[0]:    #sorted list 0 index now contains the highest number. if there is more similar highest number, then it will count
            count+=1
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
