'''import time


sec1 = time.time()
#print(sec1)
currtime = time.ctime(time.time())
print(currtime)
'''

import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here

import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    ls = []
    count = 0
    vote = list(map(int, input().split()[:N]))
    for j in vote:
        if (j != ls):
            ls.append(j)
            count += 1
        else:
            continue
    print(ls)
    l = len(ls)
    if count>=M:
        print("JANI")
    else:
        print("RAMYA")


