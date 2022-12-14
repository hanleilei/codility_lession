# -*- coding：utf-8 -*-
# &Author  hanleilei
# Lesson 2：Arrays
# P 2.1 CyclicRotation


def solution(A, K):
    """
    返回数组A经过K次旋转后的数组
    :param A: 数组
    :param K: 旋转次数
    :return: 旋转后的数组
    """
    length = len(A)
    new_list = A.copy()
    if K == 0 or length == K or length == 0:
        return new_list
    else:
        times = K % length
        for index, value in enumerate(A):
            new_list[(times + index) - length] = value
        return new_list

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(nums, k):
    # write your code in Python 3.6
    if len(nums) == 0:
        return nums
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums


