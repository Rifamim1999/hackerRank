#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    j = bill[k]
    bill.pop(k)
    sum1 = sum(bill)
    avg1 = sum1/2
    sum2 = j+sum1
    avg2 = sum2/2
    if b == avg1:
        print('Bon Appetit')
    if b != avg1:
        print(int(avg2-avg1))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
