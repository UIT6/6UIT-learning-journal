# Fibonacci
## 1 for
n = int(input("How many terms? "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a,b = b, a + b
## 2
n = int(input("Enter the number of terms you want to calculate (an int > 0): "))
a,b =0,1
i = 0
while i < n:
  print(a,end=' ')
  a, b = b ,a + b
  i += 1

## 3
f0 = 0
f1 = 1
terms = int(input('Enter the number of terms:'))

if terms <= 0:
   print('error')
elif terms == 1:
   print('series is:',f0)
elif terms == 2:
   print('series is ',f0, ',',f1,sep="")
else:
   print('Series is:',f0,',',f1,sep='',end='')
   a = f0
   b = f1
   i = 2
   while i < terms:
      c = a + b
      print(',',c,end = '' ,sep ='')
      a = b
      b = c
      i += 1

      print('F1')

def add_one(num):
   if num is 100:
      return num
   add_one(num + 1)

print(add_one(1))

## 4 (recursive + memoization)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
   if n < 0:
      raise ValueError("n must be >= 0")
   if n < 2:
      return n
   return fib(n - 1) + fib(n - 2)

def fib_sequence(count: int):
   if count < 0:
      raise ValueError("count must be >= 0")
   return [fib(i) for i in range(count)]

terms_recursive = int(input("Enter the number of terms for recursive Fibonacci: "))
print(*fib_sequence(terms_recursive))