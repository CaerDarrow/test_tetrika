import random
from math import factorial

def another_pairs_search(array, k):
    res = []
    last = ()
    start = 0
    end = len(array) - 1
    array.sort()
    while start < end:
        k_sum = array[start] + array[end]
        if k_sum == k:
            if array[start] not in last:
                last = (array[start], array[end])
                res.append(last)
            start += 1
            end -= 1
        elif k_sum < k:
            start += 1
        else:
            end -= 1
    return res


def test_pairs(f):
    for _ in range(100):
        k = random.randrange(-50, 50)
        array = [random.randrange(-50, 50) for _ in range(100)]
        res1 = sorted(map(sorted, another_pairs_search(array, k)))
        res2 = sorted(map(sorted, f(array, k)))
        try:
            assert res1 == res2
        except AssertionError:
            print(f'sum :{k}\narray: {array}\nsample output:: {res1}\nur output: {res2}')


def naive_zeros_count(n):
    zeros = 0
    num = factorial(n)
    while num % 10 == 0:
        num //= 10
        zeros += 1
    return zeros


def test_zeros(f):
    for i in range(200):
        res1 = naive_zeros_count(i)
        res2 = f(i)
        try:
            assert res1 == res2
        except AssertionError:
            print(f'sample output: {res1}\nur output: {res2}')