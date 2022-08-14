# -*- coding：utf-8 -*-
# &Author  hanleilei
# Lesson 4：Counting Elements
# P 4.2 FrogRiverOne


def solution(X, A):
    """
    返回最小的可以覆盖1到X序列的索引值
    :param X: 目标
    :param A: 数组
    :return: 最小的索引值
    """
    x_dict = {i: 0 for i in range(1, X+1)}
    for index, value in enumerate(A):
        if value in x_dict:
            del x_dict[value]
        if len(x_dict) == 0:
            return index
    return -1

def solution(X, A):
    # write your code in Python 3.6
    s = set(range(1, X+1))
    for i , v in enumerate(A):
        if v in s:
            s.remove(v)
        if len(s) == 0:
            return i
    return -1