## A+B Problem I: Calculate a + b

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

### **解题思路 (Solution Approach):**
1. **创建 `Scanner` 对象 (Create a `Scanner` object)**: 使用 `Scanner` 类来从控制台读取输入数据。
2. **循环读取输入 (Loop to read input)**: 使用 `while` 循环检查是否有下一个整数输入，这样可以确保处理每一对 `a` 和 `b`。
3. **读取并计算和 (Read and calculate the sum)**: 对于每一对 `a` 和 `b`，读取它们并计算它们的和。
4. **输出结果 (Print the sum)**: 使用 `System.out.println()` 输出 `a` 和 `b` 的和，并换行。

### **代码实现 (Code Implementation):**
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Continue reading input while there are integers to read
        while (sc.hasNextInt()) {
            int a = sc.nextInt(); // 读取第一个整数 a (Read the first integer a)
            int b = sc.nextInt(); // 读取第二个整数 b (Read the second integer b)
            int c = a + b; // 计算 a 和 b 的和 (Calculate the sum of a and b)
            System.out.println(c); // 输出结果并换行 (Print the sum and move to the next line)
        }
        sc.close(); // 关闭 Scanner 对象 (Close the Scanner object)
    }
}
```

### **`println()` 和 `print()` 说明 (Explanation of `println()` and `print()`):**
- **`System.out.println()`**: 该方法会打印内容，并在内容后添加换行符。每次使用 `println()` 时，输出会移动到下一行。  
  (This method prints the content followed by a newline. Each time you use `println()`, the output moves to the next line.)
- **`System.out.print()`**: 该方法会打印内容，但不会添加换行符。如果你想在同一行打印多个内容，可以使用 `print()` 而不是 `println()`。  
  (This method prints the content without a newline. If you want to print multiple things on the same line, you would use `print()` instead of `println()`.)

---
