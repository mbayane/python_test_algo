"""
There are a number of people who will be attending ACM-ICPC World Finals
. Each of them may be well versed in a number of topics
. Given a list of topics known by each attendee, presented as binary strings,
 determine the maximum number of topics a 2-person team can know.
  Each subject has a column in the binary string, and a '1' means the subject is known
   while '0' means it is not. Also determine the number of teams that know the maximum number of topics.
    Return an integer array with two elements. The first is the maximum number of topics known,
     and the second is the number of teams that know that number of topics.

Example:
    n=3
    topics= ['10101', '11110','00010']

The attendee data is aligned for clarity below:
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#


def acm_team(topics):
    # Write your code here
    max_number_of_topic = 0
    number_of_team = 0
    for i in combinations(topics, 2):
        s = bin(int(i[0], 2) | int(i[1], 2)).count('1')
        if max_number_of_topic < s:
            max_number_of_topic = s
            number_of_team = 0
        if s == max_number_of_topic:
            number_of_team += 1
    return max_number_of_topic, number_of_team


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acm_team(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

