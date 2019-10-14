#Ex1___________________________________________________
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

#at_three = intscts(square, 3)
#at_three(triple)
#at_three(incr)
#at_one = intscts(identity, 1)
#at_one(square)
#at_one(triple)


#Ex2___________________________________________________
def add(g1, g2):
  def g(y):
    return g1(y) + g2(y)
  return g

identity = lambda x:x
square = lambda x:x**2

#a1 = add(identity, square)
#a1(4)
#a2 = add(a1, identity)
#a2(4)
#a2(5)
#a3 = add(a1, a2)
#a3(4)


#Ex3___________________________________________________
def f():
  def g():
    def h():
      return 3
    return h
  return g

f()()(3)
