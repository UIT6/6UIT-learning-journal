# A+B问题Ⅳ学习记录

## 题目描述 | Problem Description
你的任务是计算若干整数的和。  
Each line of input begins with an integer `N`, representing the number of integers that follow.

**输入描述 | Input**  
- 每行第一个整数为`N`，表示这一行后面有`N`个数。
- 当`N=0`时，表示输入结束（且这一行不需要计算）。

**输出描述 | Output**  
- 对于每一行输入，输出这`N`个数的和，每个结果占一行。

**输入示例 | Example Input**
```
4 1 2 3 4
5 1 2 3 4 5
0
```

**输出示例 | Example Output**
```
10
15
```

---

## 我的解法 | My Solution

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 持续读取输入，直到输入结束
        while (sc.hasNextInt()) {
            int i = sc.nextInt(); // 读取每行的第一个数，表示后面要读取的数字个数
            if (i == 0) {
                break; // 如果第一个数是0，则结束输入
            }
            int sum = 0; // 用来累计本行输入的数值之和
            for (int q = 0; q < i; q++) {
                sum += sc.nextInt(); // 连续读取i个数，并累加到sum中
            }
            System.out.println(sum); // 输出当前这一行的总和
        }
        sc.close(); // 关闭Scanner，释放资源
    }
}
```

---

## 知识点总结 | Key Points Learned

### 1. 小批量读入数据 Small Batch Input
- 这种输入模式经常出现在竞赛题、面试题中：  
  **一行开头的数字N，控制后面读取N个数据。**
- 处理方法一般是：
  - 先读N。
  - 再用循环读接下来的N个数。
- **场景**：需要一次性处理一小组数据，不是整体读完再处理。

### 2. 终止条件 Termination Condition
- 特别注意：**遇到0要直接结束，不做任何计算**。
- `if (i == 0) { break; }` 是一个非常典型的用法。

### 3. 三元运算符优化 Optional Ternary Operator
- 这道题最后输出时，也可以用**三元运算符**简化（虽然没必要这么做，但理解很重要）：

```java
System.out.println(i == 0 ? "" : sum);
```
- 不过这里因为`i == 0`时已经`break`了，所以实际上三元运算符**没必要引入**。
- 更合适的应用场景是：**需要判断是否输出，或者在一行里处理不同输出情况时。**

### 4. 细节规范细节 Code Style Tips
- 使用 `sc.hasNextInt()` 而不是 `sc.hasNext()`，更严谨，避免非整数输入导致异常。
- 处理完输入后记得调用 `sc.close()`，是良好的资源管理习惯。


---

**Q1**：小批量输入在多组数据混合输入时，如何避免出错？  
**Q2**：能不能用while(true)结构代替while(sc.hasNextInt())？区别在哪里？  
**Q3**：除了三元运算符，还有哪些简化if-else结构的方法？
