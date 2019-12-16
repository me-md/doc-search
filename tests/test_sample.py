import pytest
from expects import *

def test_example():
    result = 3
    expected_result = 3

    assert result == expected_result

def test_expects():
    array = ['1']
    one = array[0]

    expect(array).not_to(be_empty)

    expect(1).to(equal(1))

    expect(lambda: foo).to(raise_error(NameError))
