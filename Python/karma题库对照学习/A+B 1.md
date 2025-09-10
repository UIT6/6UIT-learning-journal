
---

# A+B Problem I: Calculate a + b (Python)

### **题目描述 (Problem Description):**

计算 `a` 和 `b` 的和。输入包含一系列的 `a` 和 `b` 对，每一对占一行，用空格隔开。对于每一对 `a` 和 `b`，输出它们的和，每一行显示一个结果。

### **输入示例 (Input Example):**

```
3 4
11 40
```

### **输出示例 (Output Example):**

```
7
51
```

---

## **解题思路 (Solution Approach):**

1. **循环读取输入 (Loop to read input)**

   * 可用 `sys.stdin` 来迭代每一行输入，适合多行输入/文件输入。

2. **拆分和转换 (Split and Convert)**

   *  `split()` 将输入的字符串按空格拆分成列表。
   * `int()` 把拆分后的字符串转换为整数。


---

## **Python 代码实现:**

```python
#学过JAVA进阶版
import sys  # 引入 sys 模块，用于读取标准输入

# 遍历每一行输入
for line in sys.stdin:
    # 去掉首尾空白字符并按空格拆分
    a, b = line.strip().split()
    # 转换为整数并计算和，输出结果
    print(int(a) + int(b))
```

```python
#没学过java婴儿版
while True:  
    try:
        line = input()            # 读取一行文字
        numbers = line.split()    # 按空格拆成两个字符串
        a = int(numbers[0])       # 第一个数字
        b = int(numbers[1])       # 第二个数字
        print(a + b)            
    except EOFError:              # 输入结束时退出循环
        break
```
---

## **Python 知识点总结 **

1. **模块导入 (Module Import)**

   * `import sys`：导入 Python 系统模块sys，sys可以使用 `sys.stdin` 读取标准输入。

2. **标准输入迭代 (Standard Input Iteration)**

   * `for line in sys.stdin:` 遍历输入的每一行

3. **字符串处理 (String Processing)**

   * `line.strip()`：去掉首尾空白字符（换行符、空格等）。
   * `line.split()`：按空白字符拆分字符串成列表。

4. **类型转换 (Type Conversion)**

   * `int()`：将字符串转换为整数。

---

## **问题与解决**
1. **模块导入是必须的吗？还有哪些模块？**
    - 不是必须的，比如变量、循环、条件、函数等基础语法。但是模块可以提供非常多的额外功能，比如`sys`可以访问系统相关功能，`math`可以使用数学函数，`datetime`获取日期时间。除了Python自带的标准库模块，还有第三方模块，如`pandas`可以安装使用。

2. **拆分和转换在什么时候使用？**
    - 如本题，要求**读取一行两个数**输入的是字符串，需要用`split()`拆分，再用`int（）`转换成整数。如果输入的直接是数字就不用。**处理外部输入的文本时，拆分和转换几乎是必做的。**

3.  **大括号去哪儿了？**
    - Python用缩进代替了大括号，隐式标记啦~**记得统一缩进**
  
   

   
