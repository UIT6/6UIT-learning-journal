# A+B问题Ⅱ 学习笔记 | A+B Problem II Study Notes

---

## 1. `for` 循环（`for` Loop）

**语法格式 (Syntax)：**  
```java
for (初始化语句; 条件判断; 操作) {
    // 循环体 (code block)
}
```

一般情况下，初始化值从0开始。如果希望循环执行 `n` 次，标准写法是：

```java
for (int i = 0; i < n; i++) {
    // i从0到n-1，共执行n次
}
```
- `int i = 0`：初始化，从0开始计数。
- `i < n`：当`i`小于`n`时继续循环。
- `i++`：每次循环后，`i`自增1。

---

## 2. `++` 和 `--`（Increment and Decrement）

- `++i`（前置自增）：先将变量加1，再参与其他运算。  
  Example:  
  ```java
  int i = 99;
  int a = ++i; // a = 100
  ```

- `i++`（后置自增）：先使用当前值，之后再加1。

同理，递减操作：
- `--i`：先减1再使用。
- `i--`：先使用后减1。

---

## 3. `while` 循环（`while` Loop）

通过 `while` 循环执行 `n` 次操作：

```java
while (scanner.hasNext()) {
    int n = scanner.nextInt();
    while (n-- > 0) {
        // 循环体，当n减到0时结束
    }
}
```

- `scanner.hasNext()`：检测是否有输入。
- `n-- > 0`：每次循环后`n`减少1，当`n`为0时循环结束。

---

## 4. `do-while` 循环（`do-while` Loop）

**语法格式 (Syntax)：**
```java
do {
    // 循环体 (code block)
} while (条件判断);
```
特点：
- **至少执行一次**循环体代码。
- 先执行，再判断条件，决定是否继续。

---

## 5. 包装类型（Wrapper Classes）

将**基本数据类型**包装成**对象**，赋予更多功能，就像“给简单物体加上了人性”。

常用包装类：
- `Integer`：包装`int`
- `Long`：包装`long`
- `Short`：包装`short`
- `Byte`：包装`byte`
- `Double`：包装`double`
- `Float`：包装`float`
- `Character`：包装`char`
- `Boolean`：包装`boolean`

理解：  
> 基本数据类型 → 包装类 = 赋予简单值更多方法和行为（类似拟人化）。

---

## 6. 自动装箱与自动拆箱（Autoboxing and Unboxing）

- **自动装箱 (Autoboxing)**：基本类型 → 包装类对象  
- **自动拆箱 (Unboxing)**：包装类对象 → 基本类型

Example:
```java
Integer boxedAge = 10; // 自动装箱
int age = boxedAge;    // 自动拆箱
```
理解：
> 自动装箱：简单物品→有能力的“人”  
> 自动拆箱：有能力的“人”→简单物品

---

## 7. 数据类型转换（Data Type Conversion）

- **自动类型转换 (Automatic Conversion)**：小容量数据 → 大容量数据  
  运算时，容量小的类型会自动提升到容量大的类型。
  
- **强制类型转换 (Casting)**：大容量数据 → 小容量数据，需要手动指定。

Example:
```java
int i = 100;
byte b = (byte) i; // 强制将int转为byte
System.out.println(b); // 输出100
```
注意：  
> 强制转换可能导致数据精度丢失（precision loss）。

