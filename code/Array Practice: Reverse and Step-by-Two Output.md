
---

# 数组的倒序与隔位输出

## 🧾 题目描述

给定一个整数数组，编写一个程序实现以下功能：

1. 将输入的整数数组**倒序输出**，每个数之间用空格分隔。
2. 从正序数组中，每隔一个单位（即**索引为偶数**的元素），输出其值，同样用空格分隔。

---

## 📥 输入描述

* 第一行包含一个整数 `n`，表示数组的长度。
* 接下来一行包含 `n` 个整数，表示数组的元素。

---

## 📤 输出描述

* 首先输出倒序排列的数组元素。
* 然后输出正序数组中每隔一个单位的元素（索引为 `0, 2, 4...`）。

---

## 💡 输入示例

```
5
2 3 4 5 6
```

## ✅ 输出示例

```
6 5 4 3 2
2 4 6
```

---

## 🔍 数据范围

```
1 <= n <= 1000
```

---

## 🧩 解法一：使用数组

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 输入数组长度
        int n  = sc.nextInt();
        int[] nums = new int[n]; // 创建一个长度为 n 的数组

        // 读入数组元素
        for(int i = 0; i < n; i++){
            nums[i] = sc.nextInt();
        }

        // 倒序输出
        for(int i = nums.length - 1; i >= 0; i--){
            System.out.print(nums[i]);
            if(i > 0){
                System.out.print(" ");
            }
        }
        System.out.println(); // 换行

        // 隔位输出（索引为 0, 2, 4...）
        for (int i = 0; i < nums.length; i += 2) {
            System.out.print(nums[i]);
            if (i < nums.length - 2) {
                System.out.print(" ");
            }
        }

        sc.close();
    }
}
```

---

## 🧩 解法二：使用 ArrayList

```java
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        ArrayList<Integer> nums = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // 读取 n 个整数
        for (int i = 0; i < n; i++) {
            nums.add(sc.nextInt());
        }

        // 倒序输出
        for (int i = nums.size() - 1; i >= 0; i--){
            System.out.print(nums.get(i));
            if(i > 0){
                System.out.print(" ");
            }
        }
        System.out.println(); // 换行

        // 隔位输出（索引为 0, 2, 4...）
        for (int i = 0; i < nums.size(); i += 2) {
            System.out.print(nums.get(i));
            if (i < nums.size() - 2) {
                System.out.print(" ");
            }
        }

        sc.close(); // 关闭 Scanner
    }
}
```

---

## 🧠 知识点小结

* `int[] nums = new int[n];` 是声明并初始化数组。
* `ArrayList<Integer>` 是可变长度的整型列表，适合不确定长度的数据。
* 使用 `for (int i = 0; i < n; i++)` 可以逐个读入数组。
* `System.out.print()` 不换行，`System.out.println()` 换行。

---
