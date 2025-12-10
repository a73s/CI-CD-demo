#!/bin/python
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def log_value(a):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log(a)

def square(a):
    return a ** 2

def sin_value(a):
    return math.sin(a)

def cos_value(a):
    return math.cos(a)

def sqrt_value(a):
    if a < 0:
        raise ValueError("Square root undefined for negative values")
    return math.sqrt(a)

def percentage(percent, whole):
    """Calculates 'percent' of 'whole'."""
    return (percent * whole) / 100