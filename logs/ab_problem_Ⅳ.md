# A+B问题Ⅳ 学习记录

---

## 本次学习内容总结

### 1. 算术运算符（Arithmetic Operators）

- `+` ：加法（Addition）
- `-` ：减法（Subtraction）
- `*` ：乘法（Multiplication）
- `/` ：除法（Division）
- `%` ：取余（Modulo）

**重点说明**：
- `%`（取余运算符）用于计算两整数相除后的**余数**。
- 取余运算的参与对象**必须是整数类型**。

示例：
```java
int e = 21 % 6; // 结果是3
```
解释：`21 ÷ 6 = 3` 余 `3`，所以`21 % 6 = 3`。

---

### 2. 赋值运算符（Assignment Operators）

- `=` ：基础赋值运算符，将右边的值赋给左边的变量。

示例：
```java
int i = 0; // 将0赋值给i
```

**划重点**：
- 赋值永远是**右给左**。
- 通常把右边表达式的结果赋给左边变量。

---

#### 复合赋值运算符（Compound Assignment Operators）

- `sum += i;` 等价于 `sum = sum + i;`
- `sum -= i;` 等价于 `sum = sum - i;`
- `sum *= i;` 等价于 `sum = sum * i;`
- `sum /= i;` 等价于 `sum = sum / i;`
- `sum %= i;` 等价于 `sum = sum % i;`

**优点**：复合赋值运算可以让代码更简洁，同时避免重复书写变量名，减少出错机会。

---

### 3. 三元运算符（Ternary Operator）

语法格式：
```java
{expression} ? {if-true-element} : {if-false-element};
```

- `{expression}`：一个条件表达式，最终返回`true`或`false`。
- 如果表达式为`true`，取`?`后第一个值；
- 如果表达式为`false`，取`:`后第二个值。

示例：
```java
c = a > b ? a : b;
```
解释：
- 如果`a > b`成立，则`c = a`；
- 如果`a > b`不成立，则`c = b`。

**使用场景**：三元运算符适合处理简单的条件选择，使代码更加紧凑。

---
