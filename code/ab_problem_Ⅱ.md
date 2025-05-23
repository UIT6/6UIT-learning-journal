专# A+B问题Ⅱ | A+B Problem II

---

## 题目描述 (Problem Description)

**计算 a + b。**

- **输入描述 (Input Description)：**  
  第一行输入一个整数 **N**，表示后续会有 **N** 行，每行包含两个整数 **a** 和 **b**，中间用空格分隔。
  
- **输出描述 (Output Description)：**  
  对于输入的每一对 **a** 和 **b**，在对应的行输出它们的和。

- **输入示例 (Sample Input)：**
  ```
  2
  2 4
  9 21
  ```

- **输出示例 (Sample Output)：**
  ```
  6
  30
  ```

- **提示信息 (Notes)：**  
  注意：测试数据不仅仅一组，需要持续读取新的 **N** 和后续的 **a, b** 对。

---

## 我的解答 (My Solution)

```java
import java.util.*; //星号（*）表示导入java.util包中的所有类

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 持续读取输入，直到没有更多整数
        while (sc.hasNextInt()) {
            int n = sc.nextInt(); // 读取数据对数量

            // 如果n小于等于0，直接终止
            if (n <= 0) break;

            // 遍历n对a和b
            for (int i = 0; i < n; i++) {
                if (sc.hasNextInt()) { // 检查是否还有下一个整数
                    int a = sc.nextInt();
                    int b = sc.nextInt();
                    System.out.println(a + b); // 输出a和b的和
                }
            }
        }
        sc.close(); // 关闭Scanner，释放资源
    }
}
```

---

## 学习总结 (Study Notes)

- 使用 `while (sc.hasNextInt())` 保证程序可以**多组数据连续处理**，而不会因为一次输入完毕就退出。
- 在读取 `n` 之前，增加了 `n <= 0` 的判断，使程序在异常输入时能**更健壮**地结束。
- 每次循环内部，先检查 `hasNextInt()`，保证了输入数据的**正确性**，避免了意外错误。
- 最后 `sc.close()` 是良好的编程习惯，**及时释放资源**，避免潜在资源泄露问题。
- 整体流程清晰，代码易读，符合新手编写规范（加注释、结构合理）。

---

✅ 本题练习了 Java 中 **循环读取输入**、**基本加法运算** 和 **异常处理思维**，是巩固输入输出控制的基础练习
