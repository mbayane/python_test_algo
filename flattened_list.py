def is_not_flattened(items):
    return all(not isinstance(item, list) for item in items)


def flattened(items):
    if is_not_flattened(items):
        return items
    l = []
    for item in items:
        if isinstance(item, list):
            l.extend(item)
        else:
            l.append(item)
    return flattened(l)

# new code


# def flat_nested_list(nested_list: list):
#     flat_list = list()
#
#     def recursion(nested_list: list):
#         for l in nested_list:
#             if isinstance(l, list) or isinstance(l, tuple):
#                 recursion(l)
#             else:
#                 flat_list.append(l)
#
#     recursion(nested_list)
#     return flat_list


def test_flattened():
    test_cases = [
        ([1, 2, 3, [4, 5]], [1, 2, 3, 4, 5]),
        ([7, 9, 15, ['v', [34, 45, ['b', 'c']]]], [7, 9, 15, 'v', 34, 45, 'b', 'c']),
    ]

    for case in test_cases:
        input_list, expected = case
        result = flattened(input_list)

        print(f"{input_list} ===> Expected {expected} got result {result}: ({expected==result})")


if __name__ == '__main__':
    test_flattened()
