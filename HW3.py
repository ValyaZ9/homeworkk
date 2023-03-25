"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    a = [2, 18, -30]
    b = [15, -9, 0]
    c = [84, -14, 30]
    d = [45, 48, 0]
    count = 0

    for i in a:
        for j in b:
            for k in c:
                for l in d:
                    if i + j + k + l == 0:
                        count += 1
    return count


print(check_sum_of_four('a', 'b', 'c', 'd'))
