from math_series.series import fibonacci, fibonacci2, lucas, lucas2

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

def test3_zero():
  actual = lucas(0)
  expected = 2
  assert actual == expected

def test3_one():
  actual = lucas(1)
  expected = 1
  assert actual == expected

def test3_two():
  actual = lucas(2)
  expected = 3
  assert actual == expected

def test3_three():
  actual = lucas(3)
  expected = 4
  assert actual == expected

def test3_ten():
  actual = lucas(10)
  expected = 123
  assert actual == expected

def test4_zero():
  actual = lucas2(0)
  expected = 2
  assert actual == expected

def test4_one():
  actual = lucas2(1)
  expected = 1
  assert actual == expected

def test4_two():
  actual = lucas2(2)
  expected = 3
  assert actual == expected

def test4_three():
  actual = lucas2(3)
  expected = 4
  assert actual == expected

def test4_ten():
  actual = lucas2(10)
  expected = 123
  assert actual == expected
