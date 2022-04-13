#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):   
    # Write your code here
    distance1 = []
    distance2 = []
    count1 = 0
    count2 = 0
    for i in apples:      #in this function, first i have added the distance with a and b then put them to a new list
        j = i+a
        distance1.append(j)
    for i in oranges:
        j = i+b
        distance2.append(j)
    for k in distance1:         #after putting them into a new list i have used a for loop to check if it is in between s and t
        if all([k>=s,k<=t]):
            count1 += 1
        else:
            count1 = count1
    for k in distance2:
        if all([k<=t, k>=s]):
            count2 += 1
        else:
            count2 = count2
    print(count1)
    print(count2)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
