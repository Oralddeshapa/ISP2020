import random
import sys
import os


def quicksort(l, left, right):
    if left >= right:
        return
    i, j = left, right
    pivot = l[random.randint(left, right)]

    while i <= j:
        while l[i] < pivot: i += 1
        while l[j] > pivot: j -= 1
        if i <= j:
            l[i], l[j] = l[j], l[i]
            i, j = i + 1, j - 1
    quicksort(l, left, j)
    quicksort(l, i, right)


default = "CheckNumbs.txt"
if len(sys.argv) > 1:
    k = sys.argv[1]
    if os.path.exists(k):
        default = k
a = []
with open(default, "r") as inf:
    for x in inf:
        x = x.strip().split()
        for y in x:
            a.append(int(y))
quicksort(a, 0, len(a)-1)
print(a)