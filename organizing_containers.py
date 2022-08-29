#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

"""
David has several containers, each with a number of balls in it
. He has just enough containers to sort each type of ball he has into its own container.
 David wants to sort the balls using his sort method.

David wants to perform some number of swap operations such that:

Each container contains only balls of the same type.
No two balls of the same type are located in different containers.
"""


def organizing_containers(container):
    # Write your code here
    row = sorted([sum(x) for x in container])
    column = sorted([sum(x) for x in zip(*container)])
    return "Possible" if row == column else "Impossible"


def test_organizing_containers():
    list_cases = [
        ([[1, 1], [1, 1]], 'Possible'),
        ([[0, 2], [1, 1]], 'Impossible'),
        ([[0, 1], [1, 0]], 'Possible'),
        ([[0, 0], [1, 1]], 'Impossible'),
    ]

    for test in list_cases:
        input_, expected = test
        result = organizing_containers(input_)
        print(f"{input_} ===> Expected: {expected} got result {result}: ({expected==result})")


if __name__ == '__main__':
    test_organizing_containers()
