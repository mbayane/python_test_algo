"""
Lyrics...
Pyramids are amazing! Both in architectural and mathematical sense. If you have a computer, you can mess with pyramids
 even if you are not in Egypt at the time.
 For example, let's consider the following problem. Imagine that you have a pyramid built of numbers,
  like this one here:

  /3/
  \7\ 4
 2 \4\ 6
8 5 \9\ 3

Here comes the task...
Let's say that the 'slide down' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid
. As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23

Your task is to write a function that takes a pyramid representation as argument and returns its' largest 'slide down'.
 * With the input `[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]`
* Your function should return `23`.For example:
"""


def longest_slide_down(pyramid):
    if len(pyramid) == 1:
        return pyramid[0][0]

    last_stair = pyramid[-1]
    add_stair = []
    for i in range(1, len(last_stair)):
        add_stair.append(max(last_stair[i], last_stair[i-1]))
    pyramid[-2] = [a+b for a, b in zip(pyramid[-2], add_stair)]
    return longest_slide_down(pyramid[:-1])
