# Longest continuous interval

# [(1, 3), (6, 9), (8, 11), (2, 4)] --> (6, 11)
from typing import List


def tuple_size(t: tuple):
    return t[1]-t[0]


def merge_or_return(a: tuple, b: tuple) -> tuple:
    merged_a_b = None
    if a[0] < b[0] < a[1] < b[1]:
        merged_a_b = (a[0], b[1])
    return b if merged_a_b is None else merged_a_b


def process(list_tuple: List[tuple]) -> List[tuple]:
    for i in range(1, len(list_tuple)):
        list_tuple[i] = merge_or_return(list_tuple[i-1], list_tuple[i])
    return list_tuple


def find_max(list_tuple: List[tuple]) -> tuple:
    max_tuple = list_tuple[0]
    for i in range(1, len(list_tuple)):
        if tuple_size(list_tuple[i]) > tuple_size(max_tuple):
            max_tuple = list_tuple[i]
    return max_tuple


if __name__ == '__main__':
    _input = [(1, 3), (2, 9), (8, 11), (10, 16)]
    expected = (1, 16)
    result = find_max(process(_input))
    print(f"{_input} ===> Expected {expected} got result {result}: ({expected==result})")
