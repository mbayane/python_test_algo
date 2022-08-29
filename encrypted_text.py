"""
An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let  be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:


"""

import math

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def encryption(s):
    # Write your code here
    new_string = s.replace(" ", "")
    sqrt_s = math.sqrt(len(new_string))
    row = math.floor(sqrt_s)
    column = math.ceil(sqrt_s)
    results = []
    for i in range(column):
        results.append(new_string[i::column])
    return ' '.join(results)


def test_encryption():
    list_cases = [
        ('have a nice day', 'hae and via ecy'),
        ('feedthedog', 'fto ehg ee dd'),
        ('chillout', 'clu hlt io'),
    ]

    for test in list_cases:
        input_, expected = test
        result = encryption(input_)
        print(f"{input_} ===> Expected: {expected} got result {result}: ({expected==result})")


if __name__ == '__main__':
    test_encryption()

