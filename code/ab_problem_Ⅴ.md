# A+B问题Ⅴ学习记录

## 题目描述 | Problem Description
你的任务是计算若干整数的和。  
representing the number of integers that follow.

**输入描述 | Input**   
- 每行第一个整数为`N`，接下来N行每行先输入一个整数`M`，再在同一行输入`M`个整数
Each group of input begins with an integer`N`,representing the lines of intehers that follow.
Each line of input begins with an integer `M`, representing the number of integers that follow.

**输出描述 | Output**  
- 对于每组输入，输出这`M`个数的和，每个结果占一行，每组输出之间输出一个空行。

**输入示例 | Example Input**
```
2
5 1 2 3 4 5
4 1 3 4 5
1
2 2 1
```

**输出示例 | Example Output**
```
15

13
3
```
**提示信息 | Tips**
```
如果是输入多组信息，比如
2
3 2 1 3
1 2
3
4 2 1 3 2
3 4 2 1
2 1 3
输出则是
5

2
8

7

4
只保证组内每行数据的和之间有空行，两组数据之间并没有空行！
```

## 我的解法（法一） | My Solution Ⅰ

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // 持续读取输入，直到输入结束
        while (sc.hasNextLine()) {
            String line = sc.nextLine().trim();//先读一整行，清理干净空格，详见知识点总结1
            if (line.isEmpty()) continue; // 遇到空行跳过，详见知识点总结2
            int N = Integer.parseInt(line);//如果有内容，把它转换成整数N，详见知识点总结3
            while(N-- > 0){
                int M = sc.nextInt();
                int sum = 0;
                while(M-- >0){
                sum += sc.nexrInt();
                }
                System.out.println(sum);
                if(N > 0) System.out.println();
            }
            if(sc.hasNextLine()) sc.nextLine();//检查一下有没有遗留的换行，有就读掉，详见知识点总结4
        }    
        sc.close();
    }
}
```
## 此解法知识点总结 | Key Points Learned
```
String line = sc.nextLine().trim();//先读一整行，清理干净空格
if (line.isEmpty()) continue;//遇到空行跳过
int N = Integer.parseInt(line)//把这行的输入当成数字N
```
**1、 `.trim()`去掉这一行开头和结尾的所有空格、制表符（\t）和回车换行（\n）**

**2、 `line.isEmpty()`检查这一行是不是空的。**

**3、`Integer.parseInt(line)`把刚刚读取到的一行字符串，转换成一个整数。**

```
if(sc.hasNextLine()) sc.nextLine();
```
**4、每组数据结束后，输入流中可能残留一个没吃掉的回车符，为了保证输入流状态正常，顺手检查一下`sc.hasNextLine()`，如果有多余的换行，就“吃掉”它`sc.nextLine()`。**

## 我的解法（法二） | My Solution Ⅱ

```java
while(sc.hasNextLine()){
    String line = sc.nextLine().trim();//把读到的一整行去除首尾空白后检查
    if (line.isEmpty()) continue;//如果是空行，就跳过不处理，继续读取下一行。
    int N = Integer.parseInt(line);
    for(int i = 0; i < N; i++) {
        String[] parts =sc.nextLine().trim().split("\\s+");//转化为数组，详见知识点1
        int M = Integer.parseInt(parts[0]);//取出数组中第一个元素转化为整数M，详见知识点2
        int sum = 0;
        for(int j = 1; j <= M; j++){//从第二个元素开始遍历
            sum += Integer.parseInt(parts[j]);
        }
        System.out.println(sum);
        if(i<N - 1) System.out.println();
    }
}
```
## 此解法知识点总结 | Key Points Learned
```
String[] parts =sc.nextLine().trim().split("\\s+");//转化为数组，详见知识点1
int M = Integer.parseInt(parts[0]);//取出数组中第一个元素转化为整数M，详见知识点2
```
**1、`split("\\s+")`将字符串按空白字符拆分成数组。**
 - `.split`是把一个字符串按照指定分隔符拆分成多个部分，返回一个字符串数组 
 - `("\\s+")`是一个正则表达式，表示“一个或多个空白字符”。

**2、`(parts[0]) `取的是当前行的第一个数字**

 **3、hasNextLine（）**
-  使用 `while(sc.hasNextLine()) `的原因: 能处理完整的一组输入：会等待一行输入结束后再进行处理，符合题目按行输入的逻辑，可以清晰地判断是否进入了新的一组测试数据。
-  使用 `while(sc.hasNextInt())`存在的问题: 无法区分不同组数据：只关注下一个标记是否为整数，它不能识别一组输入的结束和新一组输入的开始，不能很好地处理按行组织的结构，可能会造成数据读取混乱。
   
 **4、避免多个 while 循环**
- 特别注意： **可以使用 `for `循环替代` while(N-- > 0) `循环 **。
- 使用 for 循环` for (int i = 0; i < N; i++)` 替代 `while(N-- > 0) `来控制每组数据的行数


---
 
