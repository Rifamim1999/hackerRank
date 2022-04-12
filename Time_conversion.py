#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = s[0]+s[1]
    mint = s[3]+s[4]
    sec = s[6]+s[7]
    ap = s[8]+s[9]
    if all([int(hour)==12,int(mint)>=00,int(sec)>=00,ap == 'AM']):
        s1="00:"+str(mint)+":"+str(sec)
        return s1
    elif all([int(hour)==12,int(mint)>=00,int(sec)>=00,ap=='PM']):
        s2 = "12:"+str(mint)+':'+str(sec)
        return s2
    elif ap=='PM':
        new_hour = int(hour)+12
        s3 = str(new_hour)+':'+mint+':'+sec
        return s3
    elif ap=='AM':
        s4 = hour+':'+mint+":"+sec
        return s4
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
