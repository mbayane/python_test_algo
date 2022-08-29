import re


def replace(match: re.match) -> str:
    repeats = int(match.group(1))
    sub_str = match.group(2)
    return decode(sub_str) * repeats


def decode(input_: str):
    return re.sub(r"(\d+)\[((?:[a-z]+|(\d+\[.*\]))*?)\]", replace, input_)


def test_decode():
    list_cases = [
        ('ab2[cd]', 'abcdcd'),
        ('xy3[e2[bf]]', 'xyebfbfebfbfebfbf')
    ]

    for test in list_cases:
        input_, expected = test
        result = decode(input_)
        print(f"{input_} ===> Expected: {expected} got result {result}: ({expected==result})")


if __name__ == '__main__':
    test_decode()
