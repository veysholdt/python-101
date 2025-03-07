"""
This is the calculator test file
"""

from calculator import add
from calculator import my_sum
from calculator import my_div

# this is an example
def test_add():
    assert add(0, 0) == 0, "result not correct"
    assert add(1, 2) == 3, "result not correct"


# add your tests here

def test_sum():
    nums = [1, 2, 34, 5646, 67, 454, 2323, 34]
    assert my_sum(nums) == sum(nums), "wrong sum :("

def test_div():
    nums = [(23,4), (23, 5), (45, 67)]
    for pair in nums:
        assert my_div(pair[0], pair[1]) == pair[0]/pair[1], "wrong div :("