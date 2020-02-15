import sys
import os


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


default = "CheckNumbs.txt"
if len(sys.argv) > 1:
    k = sys.argv[1]
    if os.path.exists(k):
        default = k
a = []
#a = [int(x) for x in input().split()]
#with open(console, "r") as inf:
with open(default, "r") as inf:
    for x in inf:
        x = x.strip().split()
        for y in x:
            a.append(int(y))
a = merge_sort(a)
print(a)