import pytest   # pytest module

def add(x, y):  # Function to add two numbers
    return x + y

@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])
def test_add_param(a, b, expected):
    assert add(a, b) == expected
