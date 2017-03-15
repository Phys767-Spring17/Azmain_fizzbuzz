from fizzbuzz import fizzbuzz
import pytest

def test_fizzbuzz_1():
    assert fizzbuzz(1) == 1

def test_fizzbuzz_34():
    assert fizzbuzz(34) == 34

def test_fizzbuzz_3():
    assert fizzbuzz(3) == 'fizz'

def test_fizzbuzz_5():
    assert fizzbuzz(5) == 'buzz'

def test_fizzbuzz_33():
    assert fizzbuzz(33) == 'fizz'

def test_fizzbuzz_50():
    assert fizzbuzz(50) == 'buzz'
