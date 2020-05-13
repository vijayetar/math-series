from math_series.series import fibonacci, fibonacci2, lucas, lucas2, sum_series, sum_series2

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

def test5_zero():
  actual = sum_series(0)
  expected = 0
  assert actual == expected

def test5_one():
  actual = sum_series(1)
  expected = 1
  assert actual == expected

def test5_two():
  actual = sum_series(2)
  expected = 1
  assert actual == expected

def test5_three():
  actual = sum_series(3)
  expected = 2
  assert actual == expected

def test5_ten():
  actual = sum_series(10)
  expected = 55
  assert actual == expected

def test6_zero():
  actual = sum_series(0, 2, 1)
  expected = 2
  assert actual == expected

def test6_one():
  actual = sum_series(1, 2, 1)
  expected = 1
  assert actual == expected

def test6_two():
  actual = sum_series(2, 2, 1)
  expected = 3
  assert actual == expected

def test6_three():
  actual = sum_series(3, 2, 1)
  expected = 4
  assert actual == expected

def test6_ten():
  actual = sum_series(10, 2, 1)
  expected = 123
  assert actual == expected

def test7_zero():
  actual = sum_series2(0)
  expected = 0
  assert actual == expected

def test7_one():
  actual = sum_series2(1)
  expected = 1
  assert actual == expected

def test7_two():
  actual = sum_series2(2)
  expected = 1
  assert actual == expected

def test7_three():
  actual = sum_series2(3)
  expected = 2
  assert actual == expected

def test7_ten():
  actual = sum_series2(10)
  expected = 55
  assert actual == expected

def test8_zero():
  actual = sum_series2(0, 2, 1)
  expected = 2
  assert actual == expected

def test8_one():
  actual = sum_series2(1, 2, 1)
  expected = 1
  assert actual == expected

def test8_two():
  actual = sum_series2(2, 2, 1)
  expected = 3
  assert actual == expected

def test8_three():
  actual = sum_series2(3, 2, 1)
  expected = 4
  assert actual == expected

def test8_ten():
  actual = sum_series2(10, 2, 1)
  expected = 123
  assert actual == expected