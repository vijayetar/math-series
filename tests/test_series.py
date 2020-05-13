from math_series.series import fibonacci
from math_series.series import fibonacci2

def test_zero():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected

def test_one():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected

def test_two():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected

def test_three():
  actual = fibonacci(3)
  expected = 2
  assert actual == expected

def test_ten():
  actual = fibonacci(10)
  expected = 55
  assert actual == expected

def test2_zero():
  actual = fibonacci2(0)
  expected = 0
  assert actual == expected

def test2_one():
  actual = fibonacci2(1)
  expected = 1
  assert actual == expected

def test2_two():
  actual = fibonacci2(2)
  expected = 1
  assert actual == expected

def test2_three():
  actual = fibonacci2(3)
  expected = 2
  assert actual == expected

def test2_ten():
  actual = fibonacci2(10)
  expected = 55
  assert actual == expected

