
---

## 一、数组（Array）

### （一）数组的特征
1. 固定大小，不能动态更改  
2. 存储相同数据类型的元素  
3. 元素在内存中连续存储  
4. 通过下标访问元素，下标从0开始  

### （二）如何声明和使用数组

- **声明数组：**

  ```java
  dataType[] arrayName;
```

* **示例：**

  ```java
  int[] nums;        // 声明一个整数数组 nums
  double[] scores;   // 声明一个浮点数数组 scores
  ```

* **说明：**

  1. `dataType` 表示数组元素的类型，如 `int`、`double`、`char` 等
  2. `arrayName` 是数组的名称

* **分配内存（初始化）：**

  ```java
  dataType[] arrayName = new dataType[分配的内存数量];
  ```

* **示例：**

  ```java
  int[] numbers = new int[3];           // 动态初始化，长度为3
  int[] numbers = {1, 2, 3};            // 静态初始化，包含初始值
  ```

* **访问数组元素：**

  ```java
  dataType value = arrayName[索引];
  ```

* **示例：**

  ```java
  int value = arr[2];   // 访问数组 arr 的第3个元素
  ```

* **修改数组元素：**

  ```java
  arrayName[索引] = 新值;
  ```

* **示例：**

  ```java
  arr[0] = 100;        // 修改第一个元素为 100
  ```

* **获取数组长度：**

  ```java
  int length = arrayName.length;
  ```

---

## 二、ArrayList

* `ArrayList` 是 `java.util` 包中的类，支持动态增删元素。

* **导入和创建：**

  ```java
  import java.util.ArrayList;

  ArrayList<Integer> arrayName = new ArrayList<Integer>();
  ```

* **常用操作：**

  1. **添加元素：**

     ```java
     arrayName.add(元素);
     ```

     示例：

     ```java
     nums.add(10);
     ```

  2. **获取元素：**

     ```java
     int value = nums.get(0);
     ```

  3. **删除元素：**

     ```java
     nums.remove(1);   // 删除第2个元素（索引为1）
     ```

  4. **获取大小：**

     ```java
     int size = nums.size();
     ```

  5. **遍历元素（增强型for循环）：**
* **nums** 就是整个班级队列，所有同学都排在那里；
* **num** 就是临时的“审问房间”，每次把一个同学请进去“审问”；
* **Integer** 就是同学的“身份标签”，告诉你这些同学的类型是“高中生”（基本属性）。
     ```java
     for (Integer num : nums) {
         System.out.println(num);
     }
     ```

---

