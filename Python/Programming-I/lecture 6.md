## Outline

* More on assignment （赋值进阶）
* Output revisited （输出复习）
* Input （输入）
* Types in Python （Python 数据类型）
* Type conversions （类型转换）

---

## 1️⃣ More on Assignment

### Swapping two values

#### Example that **doesn’t work**

```python
x = 2
y = 3
x = y
y = x
print(x, y)
# Output: 3, 3 ❌
```

* 问题：直接赋值会覆盖原来的值，导致交换失败。

#### Correct way using temporary variable

```python
x = 2
y = 3
temp = x
x = y
y = temp
print(x, y)
# Output: 3, 2 ✅
```

### Multiple assignment

```python
x, y = 10, 20
# x = 10, y = 20
```

* 所有右侧表达式先计算，然后依次赋值。
* 可以用多重赋值来**交换变量**

```python
x, y = 25, 36
x, y = y, x
print(x, y)
# Output: 36, 25
```

---

## 2️⃣ Output Revisited

* `print()` 函数用于输出内容。
* 默认输出到标准输出（通常是屏幕）。
* **打印变量与字符串的区别**

```python
print('euro_dollar_conversion')  # 输出字符串
print(euro_dollar_conversion)    # 输出变量值
```

---

## 3️⃣ Input
* Python 3.x 中使用 `input()` 获取用户输入（返回 **字符串类型**）

```python
name = input('Enter your name: ')
print('Hello, ' + name + '.')
```

* **注意空格处理**

  * 用 `+` 拼接可以去掉多余空格：

```python
print('Hello, ' + name + '.')
```

* 示例：多轮交互

```python
age = input('What is your age? ')
print('Wow, ' + name + '! Your age is ' + age + '.')
```

* **常见问题示例**

```python
number = input('Enter an int: ')
print('Twice the number is', number * 2)
```

* 如果用户输入 `25`，输出是：

```
Twice the number is 2525
```

* ❌ 原因：`input()` 返回字符串类型，`* 2` 对字符串进行重复操作，而不是数字乘法。
* ✅ 解决方法：先用 `int()` 转换为整数

```python
number = int(input('Enter an int: '))
print('Twice the number is', number * 2)
```

* 输出：

```
Twice the number is 50
```




---

## 4️⃣ Types in Python

* 常用类型：

  * `int` ：整数（5, -234）
  * `float` ：浮点数（1.0, 3.14, -123.45）
  * `bool` ：布尔值（True, False）
* `type()` 函数可以查看变量类型：

```python
x = input('Enter an int: ')
print(type(x))  # <class 'str'>
```

---

## 5️⃣ Type Conversions

* 使用类型转换将值转换为另一种类型：

```python
x = int('3')  # 字符串转整数
print(x * 2)  # 6
```

* float 转 int 时会**截断而非四舍五入**

```python
int(25.9)  # 25
```

* 示例：输入整数并转换类型

```python
number = int(input('Enter an int: '))
print('Twice the number is', number * 2)
print(type(number))  # <class 'int'>
```

---

## 关键知识点 / Keywords (中英对照)

| English             | 中文            |
| ------------------- | ------------- |
| Assignment          | 赋值            |
| Multiple assignment | 多重赋值          |
| Swap values         | 交换变量          |
| Output              | 输出            |
| Input               | 输入            |
| String              | 字符串           |
| Variable            | 变量            |
| Data type           | 数据类型          |
| Integer             | 整数            |
| Float               | 浮点数           |
| Boolean             | 布尔            |
| Type conversion     | 类型转换          |
| Casting             | 类型转换 / 强制类型转换 |
| `type()` function   | `type()` 函数   |

---
