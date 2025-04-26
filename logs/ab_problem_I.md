# A+B问题 I 学习笔记 (Java Programming)

## 1. 面向对象编程 (Object-Oriented Programming)
Java 是一门面向对象的语言。在 Java 中，类 (Class) 是对现实世界对象的抽象。例如，可以把“人”抽象为一个类 `Person`，并为其定义属性和方法：

- **属性 (Attributes)**: 类的特征，例如人的姓名、年龄、性别等。
- **方法 (Methods)**: 类的行为或功能，例如吃饭、睡觉等。

例如，定义一个 `Person` 类并创建一个实例：

```java
public class Person {
    String name;
    int age;
    String gender;

    public void eat() {
        System.out.println(name + " is eating.");
    }

    public static void main(String[] args) {
        Person liugang = new Person();  // Create an instance
        liugang.name = "Liugang";
        liugang.age = 56;
        liugang.gender = "Male";
        liugang.eat();  // Call the method
    }
}
```

## 2. 程序的基本结构 (Basic Structure of a Java Program)
Java 程序必须包含一个 `main` 方法，这是程序的入口点。每个 Java 程序至少有一个 `public class` 类和一个 `main` 方法。

```java
public class Main {  // A class named Main
    public static void main(String[] args) {  // The main method is required
        // Program logic goes here
    }
}
```

- **`public`**: The class is public and can be accessed from other classes.
- **`static`**: Indicates the method belongs to the class, not an instance.
- **`void`**: The method does not return any value.
- **`String[] args`**: Command-line arguments (optional).

## 3. 方法的组成 (Components of a Method)
一个方法由四部分组成：
- **返回类型 (Return Type)**: 指定方法的返回值类型。
- **方法名 (Method Name)**: 方法的名称。
- **形参列表 (Parameter List)**: 方法接收的输入参数。
- **方法体 (Method Body)**: 包含代码的部分。

例如：

```java
public int add(int a, int b) {
    return a + b;
}
```

## 4. 输入输出 (Input & Output)
在 Java 中，使用 `System.in` 来进行输入操作，使用 `System.out` 来进行输出操作。`Scanner` 类用于读取用户输入。

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);  // Create a Scanner object for input
        int a = sc.nextInt();  // Read an integer from user input
        int b = sc.nextInt();  // Read another integer
        System.out.println(a + b);  // Output the sum of a and b
        sc.close();  // Close the Scanner object
    }
}
```

### 常用的 `Scanner` 方法:
- `next()`: 读取下一个字符串。
- `nextInt()`: 读取下一个整数。
- `nextDouble()`: 读取下一个双精度浮点数。
- `nextLine()`: 读取下一行文本。
- `hasNext()`: 判断是否还有下一个输入项。
- `hasNextInt()`: 判断是否还有下一个整数输入项。

## 5. 变量 (Variables)
变量用于存储数据。在 Java 中，变量需要先声明后使用：

```java
int a;  // Declare a variable 'a' of type int
a = 100;  // Assign the value 100 to 'a'
int b = 200;  // Declare and initialize 'b' with 200
```

Java 中有多种数据类型：
- **整数类型 (Integer Types)**:
  - `byte`: 1 byte, range: -128 to 127
  - `short`: 2 bytes, range: -32,768 to 32,767
  - `int`: 4 bytes, range: -2^31 to 2^31-1
  - `long`: 8 bytes, range: -2^63 to 2^63-1
- **浮点数类型 (Floating-point Types)**:
  - `float`: 4 bytes, single precision
  - `double`: 8 bytes, double precision
- **字符类型 (Character Type)**:
  - `char`: Used for single characters, e.g., `char grade = 'A';`
- **布尔类型 (Boolean Type)**:
  - `boolean`: Can only be `true` or `false`.

## 6. 访问修饰符 (Access Modifiers)
Java 提供了 `public` 和 `private` 等访问修饰符来控制成员变量和方法的可见性。

- **`public`**: 公开的成员，其他类可以访问。
- **`private`**: 私有的成员，只能在当前类中访问。

```java
public class A {
    private int age;  // private member, cannot be accessed outside this class
}

public class B {
    // Cannot directly access 'age' from class A
}
```

## 7. 总结 (Summary)
本节内容涵盖了 Java 的基本面向对象概念、程序结构、方法、输入输出以及变量的使用。通过本次学习，我加深了对 Java 基础的理解，为后续深入学习打下了基础。

---

