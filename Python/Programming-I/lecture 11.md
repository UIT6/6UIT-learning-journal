# Fibonacci Series
## 1 while(basic)

```python
n = int(input("Enter the number of terms you want to calculate (an int > 0): "))
a,b =0,1
i = 0
while i < n:
  print(a,end=' ')
  a, b = b ,a + b
  i += 1
```

## 2 for
```python
n = int(input("How many terms? "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a,b = b, a + b
```

## 3 elif
```python
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
```

# actorial (not for)
 Prompt the user for a number
number = int(input(’Enter the number for which you wish
to calculate the factorial (an int >= 0): ’))
if number < 0:
print(’Error: Number entered was less than 0.’)
else:
if number == 0:
fact = 1
elif number == 1:
fact = 1
else:
fact = 1
i = 1
while i <= number:
fact *= i
i += 1
print(’Factorial of’, number, ’is’, fact)
print(’Finished!’)


# find the square root of a number
 Python program 1 to approximate the square root
 # Finding the square root of a number
 # Program prompts the user for the number
 # Uses exhaustive enumeration to find an approximate solution
 epsilon = 0.01
 step = epsilon ** 2
 numGuesses = 0
 # Prompt the user for a number
 number = float(input(’Enter the number for which you wish
 to calculate the square root: ’))
 root = 0.0
 while abs(number- root ** 2) >= epsilon and root <= number:
 root += step
 numGuesses += 1
 if numGuesses % 100000 == 0:
 print(’Still running. Number of guesses:’, numGuesses)
 print(’Number of guesses:’, numGuesses)
 if abs(number- root ** 2) < epsilon:
 print(’The approximate square root of’, number, ’is’, root)
 else:
 print(’Failed to find a square root of’, number)
 print(’Finished!’)
Exhaustive Enumeration
 Finding an approximate solution
 Python program 2 to approximate the square root
 # Finding the square root of a number
 # Program prompts the user for the number
 # Uses exhaustive enumeration to find an approximate solution
 epsilon = 0.01
 step = epsilon ** 2
 numGuesses = 0
 # Prompt the user for a number
 number = float(input(’Enter the number for which you wish
 to calculate the square root: ’))
 root = 0.0
 while abs(number- root ** 2) >= epsilon and root ** 2 <= number:
 root += step
 numGuesses += 1
 if numGuesses % 100000 == 0:
 print(’Still running. Number of guesses:’, numGuesses)
 print(’Number of guesses:’, numGuesses)
 if abs(number- root ** 2) < epsilon:
 print(’The approximate square root of’, number, ’is’, root)
 else:
 print(’Failed to find a square root of’, number)
 print(’Finished!’