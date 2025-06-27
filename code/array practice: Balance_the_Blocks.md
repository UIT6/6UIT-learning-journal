# Balance the Blocks（摆平积木）

## 🧩 问题描述

给定多个积木堆，每堆由若干积木组成。你的任务是通过移动积木，把所有的积木堆调整成相同高度，求**最少需要移动的积木数**。每次只能移动一块积木，且只能从较高的堆移到较低的堆。

### 输入描述

- 输入包含多组测试样例。
- 每组样例：
  - 第一行一个正整数 `n`（1 ≤ n ≤ 50），表示积木堆的数量；
  - 第二行包含 `n` 个整数 `h1, h2, ..., hn`，表示每堆的高度（1 ≤ hi ≤ 100）。
- 数据保证总积木数可以被 `n` 整除。
- 当 `n = 0` 时，输入结束。

### 输出描述

- 对每组样例，输出将所有积木堆变为相同高度所需的最少移动数。
- 每组输出后额外输出一个空行。

---

### ✅ 输入示例
```

6
5 2 4 1 7 5
0

```

### ✅ 输出示例
```

5

````

---

## 💡 解题思路（Java 实现）

- 使用 `Scanner` 读取多组输入；
- 利用 `ArrayList` 存储每组积木堆的高度；
- 计算平均高度；
- 遍历数组，只对**大于平均值的堆**，统计它们多出的积木数量并相加。

---

## 🧠 Java 代码实现

```java
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        while(sc.hasNext()) {
            int size = sc.nextInt();
            if (size == 0) {
                break; // 输入结束
            }

            ArrayList<Integer> list = new ArrayList<>();
            int sum = 0;

            // 输入每堆的高度
            for(int i = 0; i < size; i++) {
                int num = sc.nextInt();
                sum += num;
                list.add(num);
            }

            int avg = sum / size; // 平均高度
            int result = 0;

            // 计算比平均值多出的积木数
            for(int height : list) {  //“for-each循环”，把list中的所有元素遍历，赋值给变量 height，然后进行大括号中的指令
                if(height > avg) {
                    result += (height - avg);
                }
            }

            System.out.println(result);
            System.out.println(); // 空行
        }
    }
}
````

---

## 📎 知识点总结

* 平均值 = 总和 / 数组长度；
* 只计算高于平均值的差值；
* 注意输出格式：每组结果后要换行；
* `ArrayList` 和 `Scanner` 的基本用法。
* for-each循环，用来简洁地遍历 数组或集合 中的所有元素。
---
