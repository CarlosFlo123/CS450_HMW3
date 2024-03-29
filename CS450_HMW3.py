##################################################
## Author: Carlos Flores Valero
## Copyright: Copyright {2019}, {CS450_HMW3}
## Credits: Alex Yang
## Email: carlosfloresvalero@gmail.com
## Description: Some lambda and nested function samples
##################################################

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
    def h(x):
      print(x)
      def i():
        pass
      return i
    return h
  return g

#f()()(3)()



#Ex4___________________________________________________
def smth(g, dx):
  return lambda x: ((g(x-dx) + g(x) + g(x + dx))/3)

#square = lambda x:x**2
#print(round(smth(square, 1)(0), 3))



#Ex5___________________________________________________
def is_prime(x):
  tmp = x -1
  while (tmp > 1):
    if (x % tmp == 0):
      return False
    tmp -= 1
  return True


def cnt_cd(f):
  def g(x):
    if (x == 1):
      return 0
    elif(f(x) or f(x)):
      return 1 + cnt_cd(f)(x-1)
    else:
      return 0 + cnt_cd(f)(x-1)
  return g

#cnt_cd(lambda n,i: n % i == 0)(2)
#cnt_cd(is_prime)(2)
#cnt_cd(is_prime)(3)
#cnt_cd(is_prime)(4)
#cnt_cd(is_prime)(5)
#cnt_cd(is_prime)(20)



#Ex6___________________________________________________
def get_Digit(x):
  return x%10
def card_sum(n):
  result = 0
  i = 1
  while (n > 0):
    if (i % 2 != 0):
      result += get_Digit(n)
    else:
      if (get_Digit(n)*2 > 9):
        result += 1 + (get_Digit(n*2))
      else:
        result += get_Digit(n*2)
    n //= 10
    i += 1
  return result


#card_sum(2)
#card_sum(12)
#card_sum(42)
#card_sum(138743)
#card_sum(5105105105105100)
#card_sum(4012888888881881)
#card_sum(79927398713)



#Ex7___________________________________________________
def letter_to_n(x):
  if (x >= 'A' and x <= 'Z'):
    return ord(x)-65
  else:
    return ord(x)-97
def n_to_letter(x):
  if (x >= 26 and x <= 51):
    return chr(x+39)
  else:
    return chr(x+97)

def add(x,n):
  x = letter_to_n(x)
  while (n > 0):
    x += 1
    n -= 1
  return n_to_letter(x)
def sub(x,n):
  x = letter_to_n(x)
  while (n > 0):
    x -= 1
    n -= 1
  return n_to_letter(x)
def generator(n, operation):
  return lambda x:(operation(x,n))

#letter_to_n('a')
#letter_to_n('c')
#n_to_letter(3)
#h = generator(2, add)
#h('a')
#h = generator(3, sub)
#h('d')



#Ex8___________________________________________________
#def cyc(g1,g2,g3):
#  def h():
