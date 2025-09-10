

# A+B Problem II: Calculate a + b with N lines (Python)

### **题目描述 (Problem Description):**

第一行输入一个整数 `N`，表示接下来有 `N` 行，每一行包含一对整数 `a` 和 `b`，用空格隔开。
对于每一对 `a` 和 `b`，输出它们的和，每一行显示一个结果。
⚠️ 注意：测试数据不止一组，也就是说可能会连续输入多个 `N` 及其对应的数据。

---

### **输入示例 (Input Example):**

```
2
2 4
9 21
3
1 1
10 20
100 200
```

### **输出示例 (Output Example):**

```
6
30
2
30
300
```
---

## **Python 代码实现:**

```python
# 学过 JAVA 进阶版1
import sys

while True:
    try:
        N = int(sys.stdin.readline().strip())   # 从标准输入对象里读取一行 N
        for _ in range(N):                      # 循环 N 次
            numbers = sys.stdin.readline().split()
            a = int(numbers[0])
            b = int(numbers[1])

            print(a + b)
    except:  
        break
```
```python
# 学过 JAVA 进阶版2

import sys

while True:
    try:
        N = int(sys.stdin.readline().strip())   # 读取一行 N，.strip()去掉末尾的换行符，加不加都行，好习惯是加。
        for _ in range(N):                      # 循环 N 次
            a, b = map(int, sys.stdin.readline().split())   #.split()去掉首位空白
            print(a + b)
    except:  
        break

```
```python
# 没学过 Java 婴儿版
while True:
    try:
        N = int(input())               # 读入一个整数 N
        for _ in range(N):             # 循环 N 次
            numbers = input().split()  # 按空格拆成两个数
            a = int(numbers[0])        
            b = int(numbers[1])        
            print(a + b)               
    except EOFError:                   
        break
```



---

## **Python 知识点总结**

1. **读取整数 (Read Integer)**

   * `N = int(input())`：读入并转为整数。
   * `sys.stdin.readline()`：更适合大量输入，效率高。

2. **循环结构 (Loop Structure)**

   * `for _ in range(N):` 表示循环 N 次，变量名 `_` 表示循环变量不会用到。
3. **except为什么和try对齐？**
   *Python的语法是，**`try`必须配一个`except`（或finally）在同一级缩进**，这里`except`捕获的是整个try模块的异常，比如输入结束（EOFError）啦，空行转换失败（ValueError）啦。
4. **map**
   *`map`是python的内置函数。作用是把某函数（这一题是`int`）作用到可迭代对象的每个元素（这一题是输入行的字符串上，比如["3"，"5"]）。结果得到map对象，存着作用后的东西（这一题是转换后的俩整数，[3，5]）.**一行搞定 a、b**
5. **.strip（）和.split()**
-  *`.strip()`去掉字符串**开头和结尾的空白字符**，包括空格、`\n`换行符、`\t`制表符等
     - 例子：
     ```python
     line = "123\n"
     print(line.strip())    # "123"
     ```  
-  *`.split()`将字符串按空白符或指定分隔符切分为字符串列表
     - 例子：
     ```python 
     line = "123 456"
     print(line.split())   # ["123", "456"]
     ```

1. **方法1/2区别**


| 特性 | `numbers = ["3", "5"]  a = int(numbers[0])b = int(numbers[1])` | `a, b = map()` |
|------|----------------------------------------|----------------------------------|
| 类型转换 | 需要手动 `int(numbers[i])` | `map`自动转换，相当于把三个操作全做了 |

