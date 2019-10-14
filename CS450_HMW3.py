def incr(x):
  return (x + 1)
def triple(x):
  return (3*x)
def square(x):
  return (x*x)
def identity(x):
  return x

def intscts(f, x):
  def g(y):
    if (f(x) == y(x)):
      return True
    else:
      return False
  return g

at_three = intscts(square, 3)
at_three(triple)
at_three(incr)
at_one = intscts(identity, 1)
at_one(square)
at_one(triple)
  
