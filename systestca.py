import pytest
from part1 import calculate_interest

def test_tier1_only():
    assert calculate_interest(1000) == "30.00"

def test_tier2_boundary():
    assert calculate_interest(11000) == "380.00"

def test_tier3_boundary():
    assert calculate_interest(100000) == "3940.00"

def test_tier4():
    assert calculate_interest(110000) == "4390.00"

def test_small_amount():
    assert calculate_interest(500) == "15.00"

def test_zero():
    assert calculate_interest(0) == "0.00"

def test_float_input():
    assert calculate_interest(1500.50) == "47.52"

def test_exact_tier1_limit():
    assert calculate_interest(1000) == "30.00"

def test_exact_tier2_start():
    assert calculate_interest(1001) == "30.04"

def test_exact_tier3_start():
    assert calculate_interest(11001) == "380.04"


def test_string_input():
    with pytest.raises(ValueError, match="Deposit must not be a string."):
        calculate_interest("1000")

def test_negative_input():
    with pytest.raises(ValueError, match="Deposit cannot be negative."):
        calculate_interest(-500)


def test_invalid_type():
    with pytest.raises(ValueError):
        calculate_interest([1000])





