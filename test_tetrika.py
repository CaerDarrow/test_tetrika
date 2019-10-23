from tests import test_pairs, test_zeros


# O(n)
def search_pairs(array, k):
    pairs = {}
    res = []
    for elem in array:
        if k - elem in pairs.keys() and pairs[k - elem] == 0:
            res.append((k - elem, elem))
            pairs[elem] = 1
            pairs[k - elem] = 1
        if elem not in pairs.keys():
            pairs[elem] = 0
    return res


# O(n)
def get_zeros(n):
    five = 0
    two = 0
    zeros = 0
    for i in range(1, n + 1):
        while i % 10 == 0:
            i /= 10
            zeros += 1
        else:
            while i % 5 == 0:
                i /= 5
                five += 1
            else:
                if i % 2 == 0:
                    two += 1

    while two > 0 and five > 0:
        two -= 1
        five -= 1
        zeros += 1
    return zeros


def cypher_names():
    with open('names.txt') as f:
        names = sorted([name.strip('"') for name in f.readline().split(',')])
        result = 0
        for i in range(len(names)):
            alphabetical_sum = sum(map(lambda x: ord(x) - 64, names[i]))
            result += alphabetical_sum * (i + 1)
        print(result)


if __name__ == '__main__':
    test_pairs(search_pairs)
    print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))
    cypher_names()
    test_zeros(get_zeros)
    print(get_zeros(5))
    print(get_zeros(12))