 **Markdown** 笔记格式：

# 数据模型（Data Model）

**定义**  
一组用于描述和组织数据及其关系的概念和构造。  

**基本特征**  
提供 **structuring mechanism（类型构造器）**，类似编程语言中的类型机制。  

**两类主要模型**  
- **Logical models**：抽象于物理结构，用于组织数据。最常见：**Relational model**。  
- **Conceptual models**：完全独立于任何系统，侧重表示现实世界中的概念，常用于数据库设计早期。最常见：**Entity-Relationship model**。  

---

# 关系模型（Relational Model）

**特点**  
- 提供简单的 **declarative languages**，支持强大的数据访问与操作。  
- 具有严谨的理论基础。  

**核心概念**  
- **Relation** = 表（table）  
- **Tuple** = 行（row）  
- **Attribute** = 列（column）  
- **Domain** = 值的集合（如整数集合、20字符长度的字符串集合）  
- **Schema** = 属性集合，例如：`Info_City(City, Region, Population)`  
- **Degree** = 属性数量（列数）  
- **Cardinality** = 元组数量（行数）  

---

## 元组与属性

一个元组可以表示为：  
```

(v1, v2, …, vk)

```
其中 `vi ∈ dom(Ai)`。  

**例子**  
```

t = (Roma, Lazio, 3,000,000)
t\[City] = Roma

```

---

## 空值（Null Values）

- 当某些属性无可用信息时，用 **null value**（常记为 `?`）表示缺失数据。  

---

## 键（Key）

**定义**  
一组属性可以唯一标识一个元组。  

**条件**  
1. 同一关系中不存在两行在此属性集上值完全相同。  
2. 不存在更小的子集也能满足条件。  

**Primary Key**  
若存在多个候选键，需要选择一个作为 **primary key**。  

**例子**  
- `key(Info_City) = {City}`（如果城市名唯一）。  
- `key(Info_City) = {City, Region}`（允许重名城市存在于不同区域）。  

---

## 外键（Foreign Key）

- 若关系 **R** 中的一组属性 **Y** 是另一关系 **S** 的 **Key**，则 **Y** 是 **R 对 S 的 Foreign Key**。  
- **Referenced relation**：被引用的关系。  
- 外键建立了实体间的关联。  

**例子**  
- `EMPLOYEES(Emp#, Name, Job, …, Dept#)`  
- `DEPARTMENTS(Dept#, Name_Dept, …)`  
- 外键：`Dept# in EMPLOYEES → Dept# in DEPARTMENTS`  


**问题**
- 外键数量：0~n

- 外键可否为空：可以（除非设置 NOT NULL 或作为主键部分）

- 外键能否多个指向同一表：可以

- 一个外键能否指向多个表：不可以


---

## 参照完整性约束（Referential Integrity Constraints）

- 保证外键值必须在被引用关系中存在。
- * Foreign key referencing multiple attributes OK.  

**违反示例**  

```
t = (7899, Smith, technician, …, Dept#=50)
```

若 `DEPARTMENTS` 中不存在 `Dept#=50`，则违反参照完整性。  

**SQL**  
支持用户指定参照完整性规则及违反时的处理方式。  

---

# ✨ 总结

**Relational Model** 的核心：  
- **Relation（表）**  
- **Tuple（行）**  
- **Attribute（列）**  
- **Domain（域）**  
- **Schema（模式）**  
- **Key（键）**  
- **Foreign Key（外键）**  
- **Referential Integrity（参照完整性）**  

👉 它通过数学集合论和逻辑基础保证了数据的一致性和独立性。  
```



