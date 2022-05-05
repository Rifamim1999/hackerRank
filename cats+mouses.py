#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    diff1 = abs(z-x)
    diff2 = abs(z-y)
    w =' '
    if diff1>diff2:
        w = 'Cat B'
    if diff2>diff1:
        w = 'Cat A'
    if diff1 == diff2:
        w = 'Mouse C'
    return w

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
