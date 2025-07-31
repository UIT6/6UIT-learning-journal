--- 

# 奇怪的信 问题 学习记录 | Strange Letter Problem Study Notes

## 题目描述 | Problem Description

有一天，小明收到一张奇怪的信，信上要小明计算出给定数各个位上数字为偶数的和。
例如：5548，结果为12，等于4 + 8。
小明很苦恼，想请你帮忙解决这个问题。

One day, Xiaoming received a strange letter. The letter asks him to calculate the sum of the even digits in a given number.
For example, for the number 5548, the result is 12, which is 4 + 8.
Xiaoming is troubled and asks for your help to solve this problem.

**输入描述 | Input**

* 输入数据有多组。每组占一行，只有一个整数，保证数字在32位整型范围内。
* There are multiple groups of input. Each group consists of a single integer, and the number is guaranteed to be within the 32-bit integer range.

**输出描述 | Output**

* 对于每组输入数据，输出一行，每组数据下方有一个空行。
* For each input group, output the result in one line, followed by a blank line after each output.

**输入示例 | Example Input**

```
415326
3262
```

**输出示例 | Example Output**

```
12

10
```

---

## 😀 题目的解法 | My Solution

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 继续读取输入，直到没有更多输入
        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            int res = 0;    // 准备就绪，res用来储存计算结果
            while (n > 0) {
                int tmp = n % 10; // tmp 用来存储 n 的最后一位数字
                n /= 10;   // 让 n 少一位，接下来继续存储 n 的末尾数字
                if (tmp % 2 == 0) { // 如果为偶数，则加入计算
                    res += tmp;
                }
            }
            System.out.println(res);  // 输出结果
            System.out.println();     // 输出空行
        }
    }
}
```

---

## 🎯知识点总结 | Key Points Learned

### 1. `int tmp = n % 10;`

**原因 | Why use `int tmp = n % 10;`**

* 这个操作用于获取一个数的最后一位数字。
* This operation is used to get the last digit of a number.

### 2. `n /= 10;`

**原因 | Why use `n /= 10;`**

* 每次取完最后一位后，通过`n /= 10;`将`n`减少一位。
* After extracting the last digit, we use `n /= 10;` to remove the last digit from `n`.

### 3. `if(tmp % 2 == 0)`

**判断偶数 | Check for Even Numbers**

* 用 `tmp % 2 == 0` 来判断一个数是否为偶数，如果是偶数，则将其加入到结果中。
* Use `tmp % 2 == 0` to check if a number is even. If it is even, we add it to the result.

---






## 😀 评论区的解法 | Other Solution

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 持续读取每一行输入
        while (sc.hasNextLine()) {
            int sum = 0;

            // 读取整行数据，转为字符数组进行遍历
            for (char c : sc.nextLine().toCharArray()) {
                // 将字符c转化为对应的数字（'0'~'9' 对应 ASCII）
                // 判断是否为偶数，如果是，加入 sum；否则加0不影响结果
                sum += (c - '0') % 2 == 0 ? c - '0' : 0;
            }

            System.out.println(sum);
            System.out.println(); // 空行
        }
    }
}
```

---

## 🎯 知识点总结 | Key Concepts Learned

### 1. `for (char c : str.toCharArray())`

* 将字符串转为字符数组并逐个遍历。
* 用于逐位处理数字字符串，如 `"3262"` → `['3', '2', '6', '2']`

### 2. 字符转数字：`c - '0'`

* `'0'` 的 ASCII 值是 48，`'3' - '0'` 等于 3。
* 用于将字符数字变为真正的数值。

### 3. 三元运算符 `?:`

* `(条件) ? 值1 : 值2`：判断条件是否成立，成立则取值1，否则取值2。
* `(c - '0') % 2 == 0 ? c - '0' : 0` 表示：如果是偶数，加上这个数字；否则加0。

### 4. println 换行机制

* `System.out.println()` 会自动换行。
* 第二个 `System.out.println();` 是为了满足题目要求，每组输出间隔一行。

---

## 🧠 我的理解 | My Reflection

* `sc.nextLine().toCharArray()` 的作用是是把sc读到的数转化为的数组遍历，并将数组中元素赋值给c。是
* `(c - '0') % 2 == 0 ? c - '0' : 0` 是将c的字符转换为对应的数字，再判断是不是偶数，如果是，则作为数字加入结果。如果是奇数，则变为0（虽然也加入sum，但因为是0.所以对结果不造成影响）


---
