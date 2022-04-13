#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    renew = []
    for i in grades:
        if all([(i+2) % 5 ==0, i>=38]):   #here this line is for valuse less than 2 from multiple of 5
            j = int(i+2)
            renew.append(j)
        elif all ([(i+1) % 5 ==0, i>=38]):   ##here this line is for valuse less than 1 from multiple of 5
            j = int(i+1)
            renew.append(j)
        elif i<38:
            renew.append(i)
        else:
            renew.append(i)
    return renew

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
