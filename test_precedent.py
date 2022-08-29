def test_precedent(data: list):
    right_list = []
    left_list = []
    flowing = {}
    for val in data:
        list_value = val.split('>')
        right_value = list_value[1]
        left_value = list_value[0]
        flowing[left_value] = right_value
        right_list.append(right_value)
        left_list.append(left_value)
    start = (set(left_list) - set(right_list)).pop()
    result = start
    for _ in range(0, len(data)):
        x = flowing[start]
        result += x
        start = x
    return result


if __name__ == '__main__':
    test_list = [
        (['U>N', 'G>A', 'R>Y', 'H>U', 'N>G', 'A>R'], 'HUNGARY'),
        (['I>F', 'W>I', 'S>W', 'F>T'], 'SWIFT')
    ]
    for value in test_list:
        input_, expected = value
        result1 = test_precedent(input_)
        print(f"{input_} ==> Expected {expected} got result {result1}: {(expected==result1)}")
