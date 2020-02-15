import string
import sys
import os
import random
import argparse
import subprocess

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--task', '--choice', choices=['Quick', 'Merge', 'Split', 'Split10'], default='Quick')
    parser.add_argument('-fn', '--filename', default="CheckNumbs.txt")
    return parser


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


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    sorted_list = []
    l_index = r_index = 0
    l_length = len(left_list)
    r_length = len(right_list)
    for i in range(l_length + r_length):
        if l_index < l_length and r_index < r_length:
            if left_list[l_index] <= right_list[r_index]:
                sorted_list.append(left_list[l_index])
                l_index += 1
            else:
                sorted_list.append(right_list[r_index])
                r_index += 1
        elif l_index == l_length:
            sorted_list.append(right_list[r_index])
            r_index += 1
        elif r_index == r_length:
            sorted_list.append(left_list[l_index])
            l_index += 1
    return sorted_list


parser = createParser()
namespace = parser.parse_args(sys.argv[1:])
if namespace.task == 'Quick':
        print("Quick")
        default = "CheckNumbs.txt"
        if len(sys.argv) > 1:
            k = namespace.filename
            if os.path.exists(k):
                default = k
        a = []
        with open(default, "r") as inf:
            for x in inf:
                x = x.strip().split()
                for y in x:
                    a.append(int(y))
        quicksort(a, 0, len(a) - 1)
        print(a)
        #subprocess.call(["Laba1.py", "CheckNumbs.txt"], stdout="OutPut.txt")
elif namespace.task == 'Merge':
        print("Merge")
        default = "CheckNumbs.txt"
        if len(sys.argv) > 1:
            k = namespace.filename
            if os.path.exi(k):
                default = k
        a = []
        # a = [int(x) for x in input().split()]
        # with open(console, "r") as inf:
        with open(default, "r") as inf:
            for x in inf:
                x = x.strip().split()
                for y in x:
                    a.append(int(y))
        a = merge_sort(a)
        print(a)
elif namespace.task == 'Split':
        print("Split")
        d = {}
        default = "CheckText.txt"
        if len(sys.argv) > 1:
            k = namespace.filename
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
else:
        print("Split10")
        d = {}
        default = "CheckText.txt"
        if len(sys.argv) > 1:
            k = namespace.filename
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
        numb = list(d.items())
        numb.sort(key=lambda i: i[1])
        if len(numb) > 10:
            for x in range(10):
                print(numb[len(numb) - x - 1][0], numb[len(numb) - x - 1][1])
        else:
            for x in range(len(numb)):
                print(numb[len(numb) - x - 1][0], numb[len(numb) - x - 1][1])