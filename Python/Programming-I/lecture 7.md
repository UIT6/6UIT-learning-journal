
## 1. Comparison Operators 比较运算符

在 Python 中，比较运算符用于判断两个值之间的关系，返回布尔值（True / False）。

| 运算符  | 英文                       | 中文含义 |
| ---- | ------------------------ | ---- |
| `==` | Equals                   | 等于   |
| `!=` | Not equals               | 不等于  |
| `<`  | Less than                | 小于   |
| `<=` | Less than or equal to    | 小于等于 |
| `>`  | Greater than             | 大于   |
| `>=` | Greater than or equal to | 大于等于 |

✅ 示例：

```python
a, b, c, d = 2, 3, 10, 10
print(a < b)   # True
print(c > b)   # True
print(c < d)   # False
print(c == d)  # True
print(c != d)  # False
```

---

## 2. Conditions 条件

**条件语句 (Conditional sentences)** 由两部分组成：

* **Condition / Test 条件或测试** → 例如 *If I am hungry*
* **Action 动作** → 例如 *I will eat dinner*

👉 动作只在条件为真时执行，否则（可选）执行另一个动作。

---

## 3. Sequential Statements 顺序语句

* 程序从上到下依次执行
* 只有一条执行路径（straight-line programs 直线型程序）
* 执行到最后一条语句后结束

⚠️ 限制：只能解决简单问题。

---

## 4. Conditional Statements 条件语句

* 允许程序有多个执行路径（branching programs 分支程序）
* 基本结构：

```python
if Boolean_expression:
    statement(s)

if Boolean_expression:
    statement(s)
else:
    statement(s)

if Boolean_expression:
    statement(s)
elif Boolean_expression:
    statement(s)
else:
    statement(s)
```

📌 **说明**：

* `Boolean expression` → 任何返回 True/False 的表达式
* `statement(s)` → 任意 Python 语句块

---

## 5. Python 条件语句示例

### (1) 判断是否为 0

```python
number = int(input("Enter an int: "))
if number == 0:
    print("Number is zero")
print("Finished!")
```

### (2) 判断奇偶数

```python
number = int(input("Enter an int: "))
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
print("Finished!")
```

---

## 6. Boolean Expression 布尔表达式

* `number % 2 == 0` → 判断是否能被 2 整除
* `==` 是比较运算符
* `=` 用于赋值（⚠️ 两者不能混淆）

---

## 7. Indentation 缩进

* Python 通过缩进来表示代码块
* 同一级缩进 = 同一语句块
* 其它语言标记方式对比：

  * Pascal → `begin ... end`
  * C / Java → `{ ... }`
  * 有些语言用反写关键词，如 `if ... fi`
* Python 使用 “off-side rule” → 强制统一缩进风格

---

## 8. 应用：Currency Conversion 货币转换程序

### 算法步骤

1. Prompt the user for Euro amount 提示输入欧元金额
2. Read input and convert to int 读取输入
3. If Euro amount ≥ 0 then 如果金额大于等于 0

   * Perform conversion 执行转换
   * Print result 打印结果
4. Else → 提示用户输入必须 ≥ 0
5. Program finishes 程序结束

### Python 实现

```python
# Converting Euro to US Dollars
euro_dollar_conversion = 1.10769
euro_amount = int(input("Enter the amount in Euro: "))
print("Amount in Euro:", euro_amount)

if euro_amount >= 0:
    print("Amount in US Dollars:", euro_amount * euro_dollar_conversion)
else:
    print("Amount must be >= 0. Please try again.")
print("Finished!")
```

---

## 🔑 关键知识点 / Keywords

* **Comparison Operators 比较运算符**
* **Condition 条件 / Test 测试**
* **Action 动作**
* **Sequential Statements 顺序语句**
* **Branching Programs 分支程序**
* **Boolean Expression 布尔表达式**
* **Indentation 缩进 (Off-side rule)**

---
