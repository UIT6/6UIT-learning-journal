
---
# Leture 2
## Lecture 2 Summary: Structure of a Computer, Machine & Assembly Language, High-Level Programming, Program Translation

### 1️⃣ Structure of a Computer

* **Von Neumann Architecture**:

  * **CPU (Central Processing Unit)**: “大脑”，执行指令

    * **ALU (Arithmetic & Logic Unit)**: 执行算术和逻辑操作
    * **Registers**: 存放操作数和中间结果
    * **Control Unit**: 控制指令执行流程
    * **Bus Interface Unit**: CPU 与系统总线接口
  * **Primary Memory** (RAM/ROM)

    * **RAM**: 可读写，程序执行时加载，易失性
    * **ROM**: 只读，存放固件
  * **Secondary Memory**: 长期存储（硬盘、SSD）
  * **System Bus**: 数据传输通道，分内存总线和I/O总线，性能由宽度与速度决定
  * **I/O Mechanisms**: 输入/输出设备

### 2️⃣ Numbers in Computers

* **Decimal (Base 10)**: 我们日常使用的数字系统
* **Binary (Base 2)**: 计算机内部表示数字的方式，位（bit）为最小单位

  * 例：`11010111₂ = 215₁₀`
* **Octal (Base 8)** 和 **Hexadecimal (Base 16)**: 方便表示二进制

  * 例：`215₁₀ = 327₈ = D7₁₆ = 11010111₂`
* **Storage units**:

  * 1 KB = 2¹⁰ bytes = 1024 bytes
  * 1 MB = 2²⁰ bytes
  * 1 GB = 2³⁰ bytes
  * 依次类推到 TB, PB, EB, ZB, YB

### 3️⃣ CPU and Performance

* **Clock speed**: 赫兹 (Hz)，1 Hz = 1 cycle/sec

  * 例：2.8 GHz = 2.8 × 10⁹ cycles/sec
* **Multi-core(多核)**: 双核、四核等，提高并行处理能力

### 4️⃣ System Memory

* RAM 是按地址顺序存储数据，每个位置存一字节
* 现代计算机有 32-bit、64-bit 架构，可直接寻址的内存不同
* **Memory hierarchy**: CPU cache → RAM（存放正在运行的程序和数据） → Secondary storage（硬盘啥的）

### 5️⃣ Systems Software

* **Operating System (OS)**:

  * 接口：用户 ↔ 硬件
  * 管理资源：CPU、内存、I/O
  * 常见：Windows, Linux, macOS, iOS, Android

### 6️⃣ Machine Code & Assembly Language

* **Machine Code**: CPU 能直接理解的二进制指令
* **Assembly Language**: 用助记符替代二进制，方便人类阅读
* **特点**:

  * 低级、接近硬件
  * 复杂且难维护
  * 与特定硬件架构绑定

### 7️⃣ High-Level Languages

* 抽象程度高，接近问题领域
* 易于理解、修改、跨平台
* 例：Python, C, C++, Java, Fortran
* Python：问题导向，解释型语言

### 8️⃣ Program Translation

* **Source Program**: 程序员写的代码
* **Compilation**: 高级语言 → 机器/汇编代码

  * Compiler：完成翻译
  * 程序运行时执行机器码
* **Interpretation**: 直接执行源代码

  * Python 是解释型语言

### 9️⃣ Key 

* 计算机内部只“懂二进制”，所有高级语言最终都要翻译成机器码
* 程序员通常不用关心低级硬件细节，除非性能优化
* 高级语言提高开发效率，同时跨架构可用
* 内存、CPU、I/O 共同构成计算机运行的基础

---
# Leture 3
## Lecture 3 Summary: Primitive constructs & Programming Errors
### 1️⃣ **Structure of a Programming Language**

* **Primitive constructs**:
  * **Syntax**: 语法
    * 例：`3 + 3` 合法，`3 3` 不合法
  * **Static semantics**: 检查语法正确的表达式是否有意义

    * 例：`3.2 * 3.2` 合法，`3.2 * 'abcd'` 不合法
  * **Semantics**: 语义

    * 程序语义必须是明确的，不像自然语言可能有歧义

### 2️⃣ **Programming Errors**

* **Syntax errors（语法错误）**:

  * 最常见且不危险，解释器会指出位置
* **Static semantic errors（静态语义错误）**:

  * Python在运行时才会报错
* **Semantic errors（语义错误）**:

  * 程序能跑，但结果可能不是设计者想要的

### 3️⃣ **Python 的特性**

* **High-level**: 抽象操作，接近问题表示，而非硬件操作
* **General-purpose**: 可广泛用于多种任务，而非特定领域
* **Interpreted**: 解释执行，非编译

* **缺点**:

  * 相比编译型语言，运行慢，占用空间大
  * 对长期大型系统不一定最优

### 4️⃣ **Python 基本元素**

* Python 程序 = 定义 + 命令

* **注释**: `#` 开头的文字被忽略

### 5️⃣ **IDLE（Python 集成开发环境）**

* 提供文本编辑器 + shell + 调试器
* 功能：

  * 语法高亮、自动补全、缩进管理
  * 编辑 Python 文件 `.py`
  * 支持复制、粘贴、查找、注释代码


好的彤彤，我们来把 Lecture 4 的内容整理成小标题和摘要的形式，就像你前面 Lecture 2 的总结风格。

---
# Lecture 4 
## Summary: Other Programming Languages, Strings, Variables, Printing in Python

### 1️⃣ Other Programming Languages

* **C “Hello, world.” example**

```c
#include <stdio.h>
int main(void) {
    printf("Hello, world");
    return 0;
}
```

* **Java “Hello, world.” example**

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, world");
    }
}
```

* Python 与 C/Java 不同，更简洁且解释执行。

---

### 2️⃣ More About Strings

* 字符串可用单引号 `' '` 或双引号 `" "`。
* 如果字符串内有引号，可使用另一种引号包围，或者用 **转义字符 `\`**：

```python
'She shouted "Hello"'
"She shouted 'Hello'"
'It\'s a string'
```

**Escape sequences**：

| Escape | Output |
|--------|--------|
| `\t`   | horizontal tab |
| `\n`   | newline |
| `\'`   | single quote |
| `\"`   | double quote |
| `\\`   | backslash |
| `\b`   | backspace (删除前一个字符) |
| `\v`   | vertical tab (少用，显示为竖向空格) |
| `\a`   | bell/beep (不是所有系统都能听到) |


* **多行字符串**：用三引号 `"""..."""` 或 `'''...'''`。

---

### 3️⃣ Printing Strings

* 默认行为：

  1. 字符串间用空格分隔
  2. 输出末尾加换行

```python
print('String 1', 'String 2', 'String 3')
```

* 字符串拼接：用 `+`

```python
print('Hello' + ' ' + 'World')  # 输出 Hello World
```

* 重复字符串：用 `*`

```python
print('Ha' * 3)  # 输出 HaHaHa
```

* 修改 print 行为：

```python
print('13','9','2024', sep='-', end='++')  # 输出 13-9-2024++
```

---

### 4️⃣ Variables

* **定义**：命名的内存位置，用于存储数据，值可变。

* **赋值**：

  * `=` 是赋值符号，不是数学等号
  * 变量内容可以改变

* **变量命名规则**：

  * 字母、数字、下划线 `_`，但不能以数字开头
  * 区分大小写
  * 避免使用保留字
  * 名称应描述变量内容，但也要考虑书写方便


* **命名原则**：

  * 变量名便于理解和维护
  * 不依赖变量名本身的含义，程序运行依赖变量值

---

### 5️⃣ Printing in Python 2.x vs 3.x

* Python 3：`print()` 是函数

```python
print('Hello', 'John')
```

* Python 2：`print` 是语句

```python
print 'Hello', 'John'
```

* Python 2 可用逗号抑制换行：

```python
print 'String 1', 'String 2',
```

# Lecture 5 
## Summary: Numbers, Expressions, Arithmetic, Variables, Modules

## 1️⃣ Numbers in Python
- **Integer numbers**: `int` (e.g., 1, 20, 20000000)  
- **Floating-point numbers**: `float` (e.g., 1.5, 42.1234, 20.0)  
- Expressions with mixed types convert `int` → `float`.

## 2️⃣ Expressions
- Python interpreter can act as a calculator:
* Supports `+`, `-`, `*`, `/`, `//`, `%`, `**`
* Parentheses `()` can be used to group expressions.

## 3️⃣ Arithmetic Operators

| Operator | Operation                |
| -------- | ------------------------ |
| +        | Addition                 |
| -        | Subtraction              |
| \*       | Multiplication           |
| /        | Floating-point Division  |
| //       | Integer (floor) Division(整除，取商整数部分) |
| %        | Remainder（取余）                |
| \*\*     | Power（n次方）                    |

### Division Differences

* Python 3.x: `/` → always `float`
* Python 2.x: `/` between ints → `int`
* Floor division: `//`, Remainder: `%`

```python
>>> 23 / 3    # 7.666...
>>> 23 // 3   # 7
>>> 23 % 3    # 2
```

## 4️⃣ Powers

```python
>>> 3 ** 2   # 9
>>> 2 ** 8   # 256
```

## 5️⃣ Variables and Assignment

* Assign value to variable using `=`:


* Using undefined variable → `NameError`

```python
>>> x
NameError: name 'x' is not defined
```

### The special variable `_`

* Stores the last printed expression in interactive mode.

```python
>>> 2000 * 0.135
270.0
>>> 2000 + _
2270.0
```

* Treat `_` as read-only.

## 6️⃣ Using Numbers in Programs

* Example: area of a rectangle

```python
length = 2.7
breadth = 5.5
area = length * breadth
print('Area of rectangle is:', area)
```

* Mixed types in print: use commas `,` instead of `+` for floats/ints.

* Tax calculation example:

```python
tax_rate = 13.5
nett_price = 199.99
tax_due = nett_price * tax_rate / 100
total_price = nett_price + tax_due
print('Total price is:', total_price)
```

* Area of square and circle:

```python
length = 2.7      # side of square
radius = length / 2
pi = 3.1415927
print('Area of square is:', length ** 2)
print('Area of circle is:', pi * radius ** 2)
```

## 7️⃣ Importing the math module

```python
import math

radius = 1.35
print('Area of circle:', math.pi * radius ** 2)
print('Value of math.pi:', math.pi)
```

* `math` module provides: constants (`pi`, `e`) and functions (sqrt, factorial, trigonometric, ...)


```


