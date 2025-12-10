import sys
import pytest
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root/"src"))

from app import (
    add, subtract, multiply, divide,
    log_value, square, sin_value, cos_value, sqrt_value, percentage
)

def test_add():
    assert add(5, 6) == 11
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-3, 4) == -12
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_log_value():
    assert math.isclose(log_value(math.e), 1.0)
    assert log_value(1) == 0
    with pytest.raises(ValueError, match="Logarithm undefined for non-positive values"):
        log_value(0)
    with pytest.raises(ValueError, match="Logarithm undefined for non-positive values"):
        log_value(-10)

def test_square():
    assert square(4) == 16
    assert square(-4) == 16
    assert square(0) == 0

def test_sin_value():
    assert sin_value(0) == 0
    assert math.isclose(sin_value(math.pi/2), 1)

def test_cos_value():
    assert cos_value(0) == 1
    assert math.isclose(cos_value(math.pi), -1)

def test_sqrt_value():
    assert sqrt_value(16) == 4
    assert sqrt_value(0) == 0
    with pytest.raises(ValueError, match="Square root undefined for negative values"):
        sqrt_value(-4)

def test_percentage():
    assert percentage(50, 200) == 100
    assert percentage(0, 100) == 0
    assert percentage(100, 50) == 50