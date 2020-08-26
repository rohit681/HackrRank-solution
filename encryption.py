#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    a=len(s)
    b=a**(1/2)
    c=int(b)
    if(c==b):
        d=int(b)
    else:
        d=c+1
    while(1):
        if(c*d>=len(s)):
            break
        else:
            c+=1
    l=[];p=""
    for i in range(d):
        r=i
        for j in range(c):
            if(r<len(s)):
                p+=s[r]
            r+=d
        p+=" "
    return p


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
