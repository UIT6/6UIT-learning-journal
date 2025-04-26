# A+B问题Ⅲ | A+B Problem III

---

## 学习总结 (Study Notes)

---

### 1. if语句 (The `if` Statement)

**基本结构 (Basic Structure)：**
```java
if (condition) {
    // 当条件成立时执行的代码块 (Executed if condition is true)
} else if (anotherCondition) {
    // 如果上面的if不满足，判断这个条件 (Executed if another condition is true)
} else {
    // 如果所有条件都不满足 (Executed if all conditions are false)
}
```

- `condition` 是一个布尔表达式（Boolean expression），结果要么是 `true`，要么是 `false`。
- **流程**：如果第一个条件成立，执行对应的代码块；否则继续判断 `else if`；如果都不满足，执行 `else` 后的代码。

---

### 2. 关系运算符 (Relational Operators)

用于比较两个值的大小和关系 (Used to compare two values):

| 运算符 (Operator) | 含义 (Meaning)           |
|:-----------------|:-------------------------|
| `==`             | 相等 (Equal to)           |
| `>`              | 大于 (Greater than)       |
| `<`              | 小于 (Less than)          |
| `>=`             | 大于等于 (Greater or equal)|
| `<=`             | 小于等于 (Less or equal)   |
| `!=`             | 不等于 (Not equal to)      |

**示例 (Example)：**
```java
if (a >= b) {
    // 如果a大于等于b，执行这里
}
```

---

### 3. 逻辑运算符 (Logical Operators)

用来连接多个条件 (Used to connect multiple conditions):

| 运算符 (Operator) | 含义 (Meaning)                      |
|:-----------------|:-----------------------------------|
| `&&`             | 与 (AND)：两个条件都为真，结果才为真 (Both true → true) |
| `||`             | 或 (OR)：有一个为真，结果就为真 (Either true → true)  |
| `!`              | 非 (NOT)：取反 (Negate the condition) |

**示例 (Example)：**
```java
if (a == 0 && b == 0) {
    // 如果a和b都等于0
}
```

---

### 4. break语句 (The `break` Statement)

- **作用 (Purpose)：**  
  `break` 用来**立即终止**离它最近的循环 (`while`、`do while`、`for`)。

**示例 (Example)：**
```java
while (true) {
    if (a == 0 && b == 0) {
        break; // 跳出循环
    }
}
```

---

### 5. continue语句 (The `continue` Statement)

- **作用 (Purpose)：**  
  `continue` 并不会结束整个循环，只是**跳过当前这一次的循环体剩余部分**，直接进行下一次迭代。

**示例 (Example)：**
```java
while (scanner.hasNext()) {
    int a = scanner.nextInt();
    int b = scanner.nextInt();
    if (a == 0 && b == 0) {
        continue; // 当a和b都为0，跳过本次输出
    }
    System.out.println(a + b);
}
```

- **解释 (Explanation)：**  
  当输入的 `a` 和 `b` 都是0时，`continue` 会让程序跳过 `System.out.println(a + b);`，直接进入下一组输入。
