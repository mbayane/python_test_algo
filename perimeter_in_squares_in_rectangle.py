"""
The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum of the
 perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in the
 same manner as in the drawing:

 alternative text
Hint:
See Fibonacci sequence

Ref:
http://oeis.org/A000045

The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and
 returns the total perimeter of all the squares.

perimeter(5)  should return 80
perimeter(7)  should return 216
"""


def fib_memo(i):
    if i in memo:
        return memo[i]
    if i <= 1:
        return i
    else:
        f = fib_memo(i-1) + fib_memo(i-2)
        memo[i] = f
    return f


memo = {}


def perimeter(n):
    return 4*sum([fib_memo(i) for i in range(n+2)])


def test_perimeter():
    list_cases = [
        (5, 80),
        (7, 216),
        (20, 114624),
        (30, 14098308),
        (100, 6002082144827584333104)
    ]

    for test in list_cases:
        input_, expected = test
        result = perimeter(input_)
        print(f"{input_} ===> Expected: {expected} got result {result}: ({expected==result})")


if __name__ == '__main__':
    test_perimeter()
