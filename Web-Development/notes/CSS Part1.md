[FILES](https://github.com/UIT6/6UIT-learning-journal/blob/d375755ca12da1e8aa9bf0948cf485ff1a01d726/Web-Development/files/Lecture%203%20-%20CSS%20part%201.pdf)

## 1️⃣ CSS 概念与用途

* **CSS (Cascading Style Sheets)**：层叠样式表，用于控制 HTML 元素的显示样式。
* CSS 可以为整个网站提供一致的样式


---

## 2️⃣ CSS 的三种层级

1. **外部样式表 (External)**

   * 独立于 HTML 文档，使用 `<link rel="stylesheet" href="mystyle.css">` 引入。
   * 可同时作用于多个文档。
2. **文档/内部样式表 (Internal/Document-Level)**
    ```
   * 在 `<style>` 标签中定义于 HTML 文档的 `<head>` 中。
   * 适用于单个文档需要独特样式的情况。
   * <head>
        <style type="text/css">
            body {
                font-family: "Times New Roman", serif;
            }
            h1 {
                color: red;
                text-align: left;
            }
            p {
                color: green;
                font-size: 14px;
            }
        </style>
     </head>
    ```

3. **内联样式 (Inline)**

   * 在 HTML 元素上直接使用 `style="property:value;"`。
   * 优先级最高，但不推荐频繁使用，因为混合内容和表现。

---

## 3️⃣ CSS 语法与规则

* **规则集 (Rule Set)**：
* A CSS rule consists of **a selector** and **a declaration block**:

  ```css
  selector { property1: value1; property2: value2; ...; }
  ```
```
<!DOCTYPE html>
<html>
<head>
<style>
p {
  color: red;
  text-align: center;
} 
</style>
</head>
<body>

<p>Hello World!</p>
<p>These paragraphs are styled with CSS.</p>

</body>
</html>
```



---

## 4️⃣ CSS 选择器类型

1. **元素选择器 (Element Selector)**

   * 选择所有指定标签元素，例如：`p { color: red; text-align: center; }`
2. **ID 选择器 (ID Selector)**

   * 使用 `#id` 选择特定元素，例如：`#para1 { color: blue; }`
   * 页面中 ID 应唯一。不可以是数字
* ```
    <style>
    #para1 {
  text-align: center;
  color: red;
    }
    </style>
    </head>
    <body>
    <p id="para1">Hello World!</p>
    <p>This paragraph is not affected by the style.</p>
    ```

3. **类选择器 (Class Selector)**

   * 使用 `.classname` 选择拥有指定 class 的元素，例如：`.center { text-align: center; color:red; }`
   * 可用于多个元素。
   * eg：
```
p.center {      //p.center只匹配 <p> 标签，而且这个 <p> 标签必须有 class="center"。
  text-align: center;
  color: red;
}
</style>
</head>
<body>

<h1 class="center">This heading will not be affected</h1>
<p class="center">This paragraph will be red and center-aligned.</p> 

</body>
</html>
```

  
4. **分组选择器 (Grouping Selector)**

   * 使用逗号 `,` 将多个选择器组合，例如：`p.first-line, h1 { font-style: italic; }`

---
5. **全选择器 (Universal Selector)**
    * The universal selector (*) selects all HTML elements on the page.
```
<style>
* {
  text-align: center;
  color: blue;
}
</style>
```

## 5️⃣ 层叠顺序 (Cascading Order)

样式应用优先级（高到低）：

1. 内联样式（inline style）
2. 内部与外部样式表（internal/external）
3. 浏览器默认样式

> 如果同一属性在多个样式表中出现，**最后读取的样式**会覆盖前面的。

---

## 6️⃣ 组合器 (Combinators)
* Combinator 是 **选择器之间的连接符号**，用来描述 **元素之间的层级或关系**。

* 参考：[CSS Combinators](http://www.w3schools.com/cssref/css_ref_combinators.php)


---

###  **四种主要的 Combinator**

| Combinator | 例子        | 作用                                              |
| ---------- | --------- | ----------------------------------------------- |
| 空格 (space) | `div p`   | 选中所有 **`div` 内的 `<p>`**，不论 `<p>` 是直接子元素还是嵌套子孙元素 |
| 大于号 `>`    | `div > p` | 选中 **`div` 的直接子元素 `<p>`**，只一级，不会选孙子             |
| 加号 `+`     | `h1 + p`  | 选中紧接在 `<h1>` 后面的 **第一个 `<p>`**（相邻兄弟元素）          |
| 波浪号 `~`    | `h1 ~ p`  | 选中 `<h1>` 后面的 **所有兄弟 `<p>` 元素**，不限数量和位置         |

---

###  **例子说明**

#### 空格（后代选择器） **all the after ，不限层级**

```css
div p {
  color: blue;
}
```

```html
<div>
  <p>会变蓝</p>
  <section>
    <p>嵌套也会变蓝</p>
  </section>
</div>
```

#### 大于号（子元素选择器） **the direct son，最近的儿子**

```css
div > p {
  color: red;
}
```

```html
<div>
  <p>直接子元素，变红</p>
  <section>
    <p>嵌套子元素，不会变红</p>
  </section>
</div>
```

#### 加号（相邻兄弟选择器） **the first 同级，必须挨着**

```css
h1 + p {
  font-weight: bold;
}
```

```html
<h1>标题</h1>
<p>紧接标题的段落，加粗</p>
<p>不紧接标题，不加粗</p>
```

#### 波浪号（通用兄弟选择器）**all sibilings，所有同级**

```css
h1 ~ p {
  font-style: italic;
}
```

```html
<h1>标题</h1>
<p>所有标题后的段落，斜体</p>
<p>也是斜体</p>
```

---

## 7️⃣ 伪类 (Pseudo-classes) 与伪元素 (Pseudo-elements)

### **伪类**：基于元素状态或交互应用样式（如 hover）。
* 可以动态地改变元素样式，比如`:hover` → 鼠标悬停

`:active` → 点击时

`:visited` → 已访问链接

`:first-child` → 父元素的第一个子元素

`:last-child` → 父元素的最后一个子元素

* 示例：`a:hover { color: red; }`/* 当鼠标悬停在链接上时，文字变红 */
* 语法：selector:pseudo-class { property: value; }

*  参考：[CSS Pseudo-classes](http://www.w3schools.com/cssref/css_ref_pseudo_classes.php)

### **伪元素**：用于样式化元素的特定部分。
* 用来样式化元素的一部分内容，而不是整个元素。
* 语法：`selector::pseudo-element { property: value; }` （注意有两个冒号 `::`，CSS3 规范推荐用双冒号）
*  示例：段落`<p>`的首行文字字体20px，带下划线，背景浅绿色

  ```css
    p::first-line {
      font-size: 20px;
      text-decoration: underline;
      background-color: lightgreen;
    }
  ```


*  参考：[CSS Pseudo-elements](http://www.w3schools.com/cssref/css_ref_pseudo_elements.php)

---

## 8️⃣ CSS 属性

* CSS 提供大量可用属性，用于控制文字、布局、颜色、背景、边框、显示方式等。
* 参考：[CSS Selector & Properties](http://www.w3schools.com/cssref/css_selectors.asp) 
* 提供所有 CSS 选择器的完整列表，包括元素选择器、类选择器、ID、伪类、伪元素、属性选择器等。
* 测试工具↓
*  [Selector Tester](http://www.w3schools.com/cssref/trysel.asp)
* 

---

💡 **总结重点**：

* CSS 分离内容与表现，使网页开发更高效。
* 理解层叠顺序和选择器类型是 CSS 使用的核心。
* 外部样式表最适合网站整体统一，内联样式仅用于单个元素特殊处理。

---

