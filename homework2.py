Q1
num = []
for i in range(2000,3201):
  if (i%7 == 0) and (i%5 != 0):
    num.append(i)
print(num)

Q2
num = input("Please input a non-negative integers:")
num = int(num)
ftr = 1
if num == 0:
    ftr = ftr
else:
    for i in range(1,num+1):
      ftr = ftr * i
print(str(ftr))

Q3
n = input("Please input a positive integer:")
n = int(n)
squ = {}
i = 1

for i in range(i, n+1):
    squ[i] = i * i

print(squ)

Q4
num = input("Please input a sequence of comma-separated numbers:")
lis = num.split(',')
tup = tuple(num.split(','))
print(lis)
print(tup)

Q5
class getandprint():
    def _init_(self,s):
      self.s = s
    
    def getStr(self):
      self.s = input("Please input a string:")
      
    def printStr(self):
      print(self.s.upper())

twomethods = getandprint()
twomethods.getStr()
twomethods.printStr()

Q6
C = 50
H = 30
num = input("Please input a comma-separated sequence:")
D = num.split(',')
l = ''
Q = []

for i in D:
    l = str(round(((2 * C * int(i)) / H) ** 0.5))
    Q.append(l)
    
print(',' .join(Q))

Q7
num = input("Please input two comma-seperated number:")
i = int(num.split(',')[0])
j = int(num.split(',')[1])
arr = [[0 for y in range(j)] for x in range(i)]

for x in range(i):
    for y in range(j):
        arr[x][y] = x * y
        
print(arr)

Q8
word = input("Please input a comma-separated sequence of words:")
word = word.split(',')
word.sort()
print(','.join(word))

Q9
upw = ''
while True:
    word = input('Please input words：')
    if word != '':
        upw += '\n'
        upw += word
    else:
        break
print(upw.upper())

Q10
word = input("Please input words:")
word = word.split(' ')
word = set(word)
word = list(word)
word.sort()
print(' '.join(word))

Q25
class circle():
  pi = 3.14
    
  def __init__(self, r):
       self.r = r

circle1 = circle(5)
print('pi=\t', circle1.pi,' r=\t', circle1.r)

circle2 = circle(10)
circle2.pi = 3.1415
print('pi=\t', circle2.pi,' r=\t', circle2.r)

Q35
def printvalue():
  squ = {}
  
  for i in range(1,21):
    squ[i] = i*i

  for square in squ.values():
    print (square)
    
printvalue()

Q36
def printkey():
  squ = {}
  
  for i in range(1,21):
    squ[i] = i*i

  for number in squ.keys():
    print (number)
    
printkey()

Q37
def square():
  squ = []
  
  for i in range(1,21):
    squ.append(i*i)
  
  print(squ)

square()

Q43
tp1 = (1,2,3,4,5,6,7,8,9,10)
even = []

for i in range(0,10):
    if tp1[i] % 2 == 0:
      even.append(tp1[i])

tp2 = (even)
print(tp2)

Q51
class American(object):
    nationality = 'American'

class NewYorker(American):
    citizenship = 'NewYorker'

American1 = American()
NewYorker1 = NewYorker()
print('Is American1 an American?', isinstance(American1, American))
print('Is American1 a NewYorker?', isinstance(American1, NewYorker))
print('Is NewYorker1 an American?', isinstance(NewYorker1, American))
print('Is NewYorker1 a NewYorker?', isinstance(NewYorker1, NewYorker))

Q53
class Rectangle():
  def __init__(self, length, width):
      self.length = length
      self.width = width
    
  def area(self):
      self.area = self.length * self.width
      return self.area

rectangle1 = Rectangle(3,5)
print(rectangle1.area())

Q54
class Shape():
  def __init__(self):
    pass
    
  def area(self):
    self.area = 0
    return self.area
  
class Square(Shape):

  def __init__(self,length):
    super().__init__()
    self.length = length
    
  def area(self):
    self.area = self.length ** 2
    return self.area

square1 = Square(2)
print(square1.area())

Q56
def com():
  c = 5 / 0
  print("The result of dividing the two numbers is:", c)
  return c

try:
    com()
except ZeroDivisionError :
  print("An zerodivision error happened.")
except :
  print("Unkown Error Happened.")

Q94
given = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
out = set(given)
print(out)
