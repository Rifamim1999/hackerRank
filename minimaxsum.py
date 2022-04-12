#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here 
    arr.sort()
    len2 = int(len(arr) - 1)
    sum1= sum([arr[i] for i in range(len2)])
    arr.sort(reverse = True)

    sum2 = sum([arr[i] for i in range(len2)])
    print(sum1, sum2)
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
