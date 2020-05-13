def fibonacci(n):
  """ The function returns the nth value in the fibonacci series begins with 0"""
  a = 0
  b = 1
  new_list = [a,b]
  for i in range(n):
    c = a + b
    new_list.append(c)
    a = b
    b = c
  return new_list[n]

def fibonacci2(n):
  """ The recursive function returns the nth value in the fibonacci series begins with 0"""
  if n==0:
    return 0
  elif n==1 or n==2:
    return 1
  else:
    return (fibonacci2(n-1)+fibonacci2(n-2))


def lucas(n):
  """ The function returns the nth value in the lucas series begins with 2"""
  a = 2
  b = 1
  new_list = [a,b]
  for i in range(n):
    c = a + b
    new_list.append(c)
    a = b
    b = c
  print(new_list[n])
  return new_list[n]

def lucas2(n):
  """ The recursive function returns the nth value in the lucas series begins with 2"""
  if n==0:
    return 2
  elif n==1:
    return 1
  else:
    return (lucas2(n-1)+ lucas2(n-2))

def sum_series(n, a=0, b=1):
  """ The function returns the nth value with two optional parameters for the index 0 and 1 position. default set for starting with 0 and 1 from the fibonacci series"""
  new_list = [a,b]
  for i in range(n):
    c = a + b
    new_list.append(c)
    a = b
    b = c
  return new_list[n]

def sum_series2(n, a=0, b=1):
  """ The recursive function returns the nth value with two optional parameters a and b at index 0 and 1 position with default values of a = 0 and b = 1 from the fibonacci series. """
  if n==0:
    return a
  elif n==1:
    return b
  else:
    return (sum_series(n-1,a,b)+ sum_series(n-2,a,b))

