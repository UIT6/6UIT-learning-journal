好的，我可以帮你把 **COMP10280 Practical 1~7 的原题和参考答案（包括 Python 代码示例）** 整理出来，并保持和你作业要求一致的风格。为了便于你复习，我会把每个 Practical 的题目列出，然后给出对应的 Python 示例代码作为答案（虚拟代码，按你之前作业模式）。

---

## **Practical Sheet 1**

**题目：**

1. 安装 Python 3，并确保能运行 shell。
2. 安装 IDLE 或其他 IDE，并确保能打开 shell。
3. 使用 shell 打印 `"Hello, world."`
4. 用 IDE 创建 p1p1.py，写入程序并运行。
5. 编辑 p1p1.py 生成 p1p2.py（`Good Morning, Vietnam`）。
6. 在终端确保 `python p1p1.py` 和 `python p1p2.py` 可以运行。
7. 写一个程序打印姓名、地址、电话，保存为 p1p3.py。

**参考答案（Python 代码示例）：**

```python
# p1p1.py
print("Hello, world.")

# p1p2.py
print("Good Morning, Vietnam!")

# p1p3.py
print("Luna")
print()
print("123 Python Street")
print()
print("0123456789")
```

---

## **Practical Sheet 2**

**题目：**

1. 用单个 print 命令打印 `"Hello,"` 和 `"world."`，包括空格，保存为 p2p1.py。
2. 用单个 print 命令和字符串拼接打印 `"Hello, world."`，保存为 p2p2.py。
3. 把拼接的结果赋值给变量并打印，保存为 p2p3.py。
4. 字符索引实验，保存为 p2p4.txt。
5. 字符串切片实验（x、y 不同情况），保存为 p2p5.txt。

**参考答案（Python 代码示例）：**

```python
# p2p1.py
print("Hello,", "world.")

# p2p2.py
print("Hello," + " world.")

# p2p3.py
greeting = "Hello," + " world."
print(greeting)

# p2p4.txt 示例
word = "elephant"
print(word[0])  # 'e'
print(word[3])  # 'p'
print(word[-1]) # 't'

# p2p5.txt 示例
word = "herd of elephants"
print(word[0:4])  # 'herd'
print(word[4:4])  # ''
print(word[5:])   # 'of elephants'
print(word[:5])   # 'herd '
print(word[:])    # 'herd of elephants'
```

---

## **Practical Sheet 3**

**题目：**

1. 货币转换（变量赋值 float）。
2. 几何计算（面积、体积）。
3. 分配金额和计算不同税率，打印总额。

**参考答案（Python 代码示例）：**

```python
# p3p1.py
amount = 100.50
rate = 0.85  # 假设 EUR->GBP
converted = amount * rate
print(converted)

# p3p2.py
import math
length = 5.12
square_area = length**2
cube_volume = length**3
circle_area = math.pi * (length/2)**2
sphere_volume = (4/3) * math.pi * (length/2)**3
cylinder_volume = math.pi * (length/2)**2 * length
print(square_area, cube_volume, circle_area, sphere_volume, cylinder_volume)

# p3p3.py
amount = 100.0
large = amount * 0.6
small = amount * 0.4
tax = large * 0.135 + small * 0.23
total = amount + tax
print(total)
```

---

## **Practical Sheet 4**

**题目：**

1. 使用 `input()` 读取货币金额和汇率，计算转换。
2. 使用 `input()` 读取长度，计算几何量。
3. 读取金额，分配比例，计算税额并打印详细信息。

**参考答案（Python 代码示例）：**

```python
# p4p1.py
amount = float(input("Enter amount: "))
rate = float(input("Enter exchange rate: "))
converted = amount * rate
print("Converted amount:", converted)

# p4p2.py
import math
length = float(input("Enter length: "))
square_area = length**2
cube_volume = length**3
circle_area = math.pi * length**2
sphere_volume = (4/3) * math.pi * length**3
cylinder_volume = math.pi * length**2 * length
print(square_area, cube_volume, circle_area, sphere_volume, cylinder_volume)

# p4p3.py
amount = float(input("Enter amount: "))
large = amount * 0.6
small = amount * 0.4
tax1 = large * 0.135
tax2 = small * 0.23
total_tax = tax1 + tax2
total_amount = amount + total_tax
print(amount, tax1, tax2, total_tax, total_amount)
```

---

## **Practical Sheet 4.5**（加了输入检查）

```python
# p4-5p1.py
amount = float(input("Enter amount: "))
if amount < 0:
    print("Amount must be >= 0. Please try again.")
else:
    rate = 0.85
    converted = amount * rate
    print(converted)

# p4-5p2.py
import math
length = float(input("Enter length: "))
if length < 0:
    print("Length must be >= 0. Please try again.")
else:
    print("Area square:", length**2)
    print("Volume cube:", length**3)
    print("Circle area:", math.pi * length**2)
    print("Sphere volume:", (4/3)*math.pi*length**3)
    print("Cylinder volume:", math.pi*length**2*length)

# p4-5p3.py
income = float(input("Enter income: "))
if income < 0:
    print("Amount of income must be >= 0. Please try again.")
else:
    large = income * 0.6
    small = income * 0.4
    tax1 = large * 0.2
    tax2 = small * 0.4
    total_tax = tax1 + tax2
    net_income = income - total_tax
    print(income, tax1, tax2, total_tax, net_income)
```

---

## **Practical Sheet 5**

```python
# p5p1.py
n = int(input("Enter integer: "))
if n < 0:
    print("Number is negative.")

# p5p2.py
n = int(input("Enter integer: "))
if n >= 0:
    print("Number is non-negative.")
else:
    print("Number is negative.")

# p5p3.py
x = float(input("Enter float: "))
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# p5p4.py
n = int(input("Enter integer: "))
if n < 0:
    print("Number is negative")
elif n == 0:
    print("Number is equal to 0")
elif n <= 20:
    print("0<n<=20")
elif n <= 40:
    print("20<n<=40")
elif n <= 60:
    print("40<n<=60")
elif n <= 80:
    print("60<n<=80")
elif n <= 100:
    print("80<n<=100")
else:
    print("Number>100")

# p5p5.py
city = input("Enter town/city name: ")
if city == "Dublin":
    print("You entered Dublin. Dublin is in Leinster.")
elif city == "Belfast":
    print("You entered Belfast. Belfast is in Ulster.")
elif city == "Cork":
    print("You entered Cork. Cork is in Munster.")
elif city == "Limerick":
    print("You entered Limerick. Limerick is in Munster.")
elif city == "Derry":
    print("You entered Derry. Derry is in Ulster.")
elif city == "Galway":
    print("You entered Galway. Galway is in Connacht.")
elif city == "Lisburn":
    print("You entered Lisburn. Lisburn is in Ulster.")
elif city == "Kilkenny":
    print("You entered Kilkenny. Kilkenny is in Leinster.")
elif city == "Waterford":
    print("You entered Waterford. Waterford is in Munster.")
elif city == "Sligo":
    print("You entered Sligo. Sligo is in Connacht.")
else:
    print("Sorry, I didn’t recognise that name.")
```

---

好的，彤彤，我可以帮你从 **Practical 6 和 7** 开始重新整理答案，用 **while 循环代替 for**，完全不写 for。Python 代码风格和你作业一致，也方便你直接复习和练习。

---

## **Practical Sheet 6（while 循环版）**

```python
# p6p1.py
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a + b > 100:
    print("That is a big total!")

# p6p2.py
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

odds = []
if n1 % 2 != 0:
    odds.append(n1)
if n2 % 2 != 0:
    odds.append(n2)
if n3 % 2 != 0:
    odds.append(n3)

if len(odds) > 0:
    largest_odd = odds[0]
    i = 1
    while i < len(odds):
        if odds[i] > largest_odd:
            largest_odd = odds[i]
        i += 1
    print("Largest odd:", largest_odd)
else:
    print("No odd numbers.")

# p6p3.py
name = input("Enter your name: ")
if name == "Luna":
    print("That is a cool name!")
elif name == "Mickey Mouse" or name == "Spongebob Squarepants":
    print("Are you sure that's your name?")
else:
    print("You have a nice name.")

# p6p4.py
password = "abc123"
attempt = 0

p = input("Enter password: ")
attempt += 1
if p == password:
    print("You have successfully logged in.")
else:
    p = input("Enter password again: ")
    attempt += 1
    if p == password:
        print("You have successfully logged in.")
    else:
        p = input("Enter password third time: ")
        attempt += 1
        if p == password:
            print("You have successfully logged in.")
        else:
            print("You have been denied access.")

# p6p5.py
password = "abc123"
attempt = 1
success = False

while attempt <= 3:
    p = input("Enter password: ")
    if p == password:
        success = True
        print("You have successfully logged in.")
        break
    attempt += 1

if not success:
    print("You have been denied access.")
```

---

## **Practical Sheet 7（while 循环版）**

```python
# p7p1.py
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")

# p7p2.py
year = int(input("Enter year: "))
if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not leap year")

# p7p3.py
i = 1
while i <= 50:
    print(i, i**2)
    i += 1

# p7p4.py
i = 1
total = 0
while i <= 5000:
    total += i
    i += 1
print(total)

# p7p5.py
i = 1
total = 0
while i <= 10000:
    if i % 3 == 0 or i % 5 == 0:
        total += i
    i += 1
print(total)
```

