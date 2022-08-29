#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

import os


def count_it(a, b):
    _c = 0
    for z in zip(a, b):
        if "1" in z:
            _c += 1
    return _c


def acmTeam(topic):
    # Write your code here
    _max, _count = (0, 0)
    for i in range(len(topic)):
        for j in range(i):
            c = count_it(topic[i], topic[j])
            if c == _max:
                _count += 1
            elif c > _max:
                _max, _count = (c, 1)
    return [_max, _count]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
