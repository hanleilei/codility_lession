# -*- coding：utf-8 -*-
# &Author  hanleilei
# Lesson 5：Prefix Sums
# P 5.1 PassingCars


def solution(A):
    """
    根据数组A中车的行驶方向，确定出现多少对过路车
    :param A: 数组
    :return: 过路车的对数
    """
    reverse_list = A[::-1]
    pairs = 0
    forward_passing = 0
    zero_sign = 0
    for index, value in enumerate(reverse_list):
        if value == 0:
            forward_passing += index - zero_sign
            pairs += forward_passing
            zero_sign = index + 1
            if pairs > 1000000000:
                return -1
    return pairs

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    size = len(A)
    pairs_passed_by = 0
    zeroes = 0
    for i in range(size):
        if A[i] == 0:
            zeroes+= 1
        else:
            pairs_passed_by += zeroes
            if pairs_passed_by > 1000000000:
                return -1
    return pairs_passed_by