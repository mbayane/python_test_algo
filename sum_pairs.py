"""
Sum of Pairs
Given a list of integers and a single sum value, return the first two values (parse from the left please) in order
 of appearance that add up to form the sum.

 sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]

Negative numbers and duplicate numbers can and will appear.

NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.
"""

from itertools import combinations


class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)


def sum_pairs(ints, s):
    tmp_list = combinations(enumerate(ints), 2)

    # convertion to desired format
    c_list = [[[idx1, idx2], [arr1, arr2]] for ((idx1, arr1), (idx2, arr2)) in tmp_list]
    d = Dictlist()
    for p in c_list:
        if p[1][0]+p[1][1] == s:
            print((p[0][1],p[0][0]), p[1])
            d[(p[0][1]-p[0][0])]=p[1]
    result = sorted(d.items())[0][1] if len(d) else None
    return result[0] if result and len(result) >= 1 else None


#Solution 2


def sum_pairs(ints, s):
    num_dic = {}
    for num in ints:
        if num in num_dic:
            return [num_dic[num], num]
        else:
            num_dic[s - num] = num
