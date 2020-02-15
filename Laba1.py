import string
import sys
import os

d = {}
default = "CheckText.txt"
if len(sys.argv) > 1:
    k = sys.argv[1]
    if os.path.exists(k):
        default = k
with open(default, "r") as inf:
    for a in inf:
        a = a.strip()
        a = ''.join(ch for ch in a if ch not in string.punctuation)
        a = a.split()
        for key in a:
            if key in d:
                temp = d[key]
                del d[key]
                temp += 1
                d[key] = temp
            else:
                d[key] = 1
    # a = a.lower().split()
    for x in d:
        print(x, " ", d[x])
