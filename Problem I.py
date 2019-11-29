"""a_triplet = map(int, input().split())
b_triplet = map(int, input().split())
alice_points = 0
bob_points = 0
for a_val, b_val in zip(a_triplet, b_triplet):
    if a_val < b_val:
        bob_points += 1
    elif a_val > b_val:
        alice_points += 1
print(alice_points, bob_points)"""

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    ar.sort()
    ar.append('#')
    i = 0
    while i<n:
        if ar[i]==ar[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    return count
print(sockMerchant(3,5))
"""if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()"""