print("hi")

def fibonacci(n):
  # """ The function returns the nth value in the fibonacci series begins with 0"""
  a = 0
  b = 1
  new_list = [a,b]
  for i in range(n):
    c = a + b
    new_list.append(c)
    a = b
    b = c
  print(new_list)
  return new_list[n]

# fibonacci(10)

# def lucas(n):
#   """ The function returns the nth value in the lucas series begins with 1"""
#   pass

# def sum_series():
#   pass
