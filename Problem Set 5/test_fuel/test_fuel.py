import pytest
from fuel import valid_input, convert, gauge

def test_valid_input():
    assert valid_input("1/2") == True
    assert valid_input("9/1") == False
    with pytest.raises(ValueError):
        valid_input("1/w")

def test_convert():
    assert convert(1, 2) == 50
    assert convert(2, 3) == 67
    with pytest.raises(ZeroDivisionError):
        convert(55, 0)

def test_gauge():
    with pytest.raises(SystemExit):
        gauge(99)
        gauge(50)
        gauge(1)