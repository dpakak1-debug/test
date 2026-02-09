import pytest
from math_utils import MathUtils

@pytest.fixture
def math_utils():
    return MathUtils()

def test_add(math_utils):
    assert math_utils.add(2, 3) == 5
    assert math_utils.add(-2, 2) == 0
    assert math_utils.add(-2, -3) == -5

def test_subtract(math_utils):
    assert math_utils.subtract(5, 3) == 2
    assert math_utils.subtract(3, 5) == -2
    assert math_utils.subtract(4, 4) == 0

def test_multiply(math_utils):
    assert math_utils.multiply(2, 3) == 6
    assert math_utils.multiply(5, 0) == 0
    assert math_utils.multiply(-2, 3) == -6

def test_divide_valid(math_utils):
    assert math_utils.divide(6, 3) == 2.0
    assert math_utils.divide(-5, 2) == -2.5

def test_divide_by_zero(math_utils):
    assert math_utils.divide(10, 0) == -1.0
