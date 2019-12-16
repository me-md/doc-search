import pytest
from expects import *

def test_example():
    result = 3
    expected_result = 3

    assert result == expected_result

def test_expects():
    array = []
    one = 1
    expect(array).to(be_empty)
    expect(1).to(equal(1))
