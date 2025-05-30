# Markdown常用符号与注意事项总结

## 1. 基本格式对照表

| Markdown语法         | 功能说明           | 示例                           | 渲染效果       |
|--------------------|----------------|------------------------------|------------|
| `# 一级标题`          | 一级标题（最大）      | `# 标题`                        | # 标题 |
| `## 二级标题`         | 二级标题             | `## 标题`                       | ## 标题 |
| `### 三级标题`        | 三级标题             | `### 标题`                      | ### 标题 |
| `**加粗内容**`        | 加粗               | `**加粗**`                     | **加粗** |
| `*斜体内容*`          | 斜体               | `*斜体*`                       | *斜体* |
| `1. 有序列表项`       | 有序列表（数字+英文点） | `1. 第一项`<br>`2. 第二项`        | 1. 第一项<br>2. 第二项 |
| `- 无序列表项`         | 无序列表            | `- 项目A`<br>`- 项目B`          | - 项目A<br>- 项目B |
| `` `行内代码` ``      | 行内小代码          | `` `代码` ``                   | `代码` |
| ``` ```多行代码``` ```| 块级代码块（多行）    | <pre>```<br>多行代码<br>```</pre> | 多行代码块 |
| `| 表头 | 表头 |`<br>`| --- | --- |`<br>`| 内容 | 内容 |` | 表格             | 见上方对照表 |

---

## 2. 特殊问题讲解

### 2.1 为什么 `**1.**` 不会加粗？
- `1.` ➔ 数字+英文点，Markdown自动当成有序列表识别
- 导致无法被识别为普通文字加粗

### 2.2 如果**想加粗英文点号的数字**怎么办？
- 在`.`前加一个转义符 `\`：
```markdown
**1\.**
```
效果：**1.**

✅ 这样就能成功加粗，而不会被解析成列表。

### 2.3 为什么 `**1、**` 可以直接加粗？
- `1、` 里面是数字+中文顿号（、）
- Markdown不会把它识别成列表 ➔ 正常渲染成加粗文字。



### 2.4 如果想显示<strong>&#124;&#124;</strong>怎么办？
- Github里，&#124;会被识别成表格列的一部分或被忽略，要用HTML实体编码`&#124;`
- 如果想要加粗显示，用HTML实体编码`<strong>&#124;&#124;</strong>`
---

## 3. 小技巧总结

- 标题越多`#`越多（一般到`#`×6）
- 行内代码用单个反引号 `` `代码` ``
- 多行代码（比如Java程序块）用三重反引号：

- 表格要对齐美观，可以适当加空格，不影响渲染。
- 写列表项时，记得后面加个空格更标准，比如：
  ```markdown
  1. 项目A
  2. 项目B
  ```

---

