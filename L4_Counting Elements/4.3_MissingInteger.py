# -*- coding：utf-8 -*-
# &Author  hanleilei
# Lesson 4：Counting Elements
# P 4.3 MissingInteger


def solution(A):
    """
    返回数组A中未出现的最小的正整数
    :param A: 数组
    :return: 未出现的最小的正整数
    """
    x_dict = {i: 0 for i in A}
    length = len(x_dict)
    for i in range(1, len(x_dict) + 1):
        if i not in x_dict:
            return i
    return length + 1

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    a = [0] * 1000000
    for i in A:
        if i > 0:
            a[i-1] = 1
    for i in range(len(a)):
        if a[i] == 0:
            return i+1