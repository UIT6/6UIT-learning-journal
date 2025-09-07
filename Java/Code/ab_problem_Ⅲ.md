# A+B问题Ⅲ 学习记录

## 题目描述

你的任务是**计算每对输入的a和b的和**。

- **输入描述**：输入中每行是一对整数a和b，以空格分隔。当输入一对`0 0`时，表示输入结束，这一对不需要计算。
- **输出描述**：对每对a和b，输出它们的和，每个结果占一行。

---

## 输入示例
```
2 4
11 19
0 0
```

## 输出示例
```
6
30
```

---

## 我的答案

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // 创建Scanner对象，读取标准输入

        // 循环读取输入，只要还有整数输入就继续
        while (sc.hasNextInt()) {
            int a = sc.nextInt(); // 
            int b = sc.nextInt(); // 

            // 如果遇到a和b都为0，终止循环，不再计算
            if (a == 0 && b == 0) {
                break;
            }

            // 输出a+b的结果
            System.out.println(a + b);
        }

        sc.close(); 
    }
}
```

---

## 关键知识点总结

  **continue语句**
   - 终止当前这一次循环，跳过剩下的代码，直接进入下一次循环判断。
