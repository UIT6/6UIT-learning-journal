
## 🎯 SQL Part 1 全知识点覆盖速查表（含课件原文引用）

| #  | 知识点                            | ✅ 要点总结                             | ⚠️ 常见陷阱 / 出题套路               | 💡 记忆技巧          | 📜 课件原文句子 / 相关语句                                                                                                                            |      |          |
| -- | ------------------------------ | ---------------------------------- | ---------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ---- | -------- |
| 1  | SQL 定义                         | SQL = DDL + DML + 可扩展功能            | 误说 SQL 只是查询语言                | “结构三合一：定义、操作、控制” | *“The name is an acronym for Structured Query Language”*                                                                                    |      |          |
| 2  | 历史                             | 1974 SEQUEL → 1981 SQL/DS → 标准化    | 混淆 proposal / implementation | “7提8实9标”         | *“First proposal: SEQUEL (IBM Research, 1974)”* / *“First implementation in SQL/DS (IBM, 1981)”*                                            |      |          |
| 3  | SQL 标准版本                       | SQL-86, SQL-89, SQL-92, SQL-99     | 出题写错版本名称                     | “86起步，92改进”      | *“First standard, 1986, revised in 1989 (SQL-89)”* / *“Second standard, 1992 (SQL-2 or SQL-92)”*                                            |      |          |
| 4  | SQL 分类                         | 包含 DDL、DML                         | 误说只有 DML                     | “SQL 是定义 + 操作语言” | *“Far richer than a query language: both a DML and a DDL”*                                                                                  |      |          |
| 5  | Domain（域）                      | 定义属性类型，可默认、可约束                     | 把 domain 当表                  | “域是列的类型模板”       | *“Domains specify the datatype of attributes”*                                                                                              |      |          |
| 6  | Elementary domains             | 字符 / 数值 / 时间等                      | 混错误类型                        | “字、数、时三类”        | *“Examples elementary domains … character … bit … exact numeric … approximate numeric … temporal instants … temporal intervals”*            |      |          |
| 7  | Temporal domains               | date / time / timestamp / interval | 混淆 interval 单位               | “时间 = 瞬间 + 区间”   | *“Temporal instants … date time timestamp … Temporal intervals … units of time”*                                                            |      |          |
| 8  | Domain 语法                      | `CREATE DOMAIN …`                  | 忘写 AS / default              | “先名后型再限”         | *“Syntax: create domain DomainName as ElementaryDomain [ DefaultValue ] [ Constraints ]”*                                                   |      |          |
| 9  | Default Values                 | 未指定列时使用默认值                         | 误以为必须显式赋值                    | “没填就用我”          | *“Default domain values … define the value that the attribute must assume when a value is not specified during row insertion”*              |      |          |
| 10 | Schema 定义                      | 模式包含对象集合                           | 混成实例 / 表                     | “六大件：域表索断视权”     | *“A schema is a collection of objects: domains, tables, indexes, assertions, views, privileges”*                                            |      |          |
| 11 | Schema 语法                      | `CREATE SCHEMA`                    | 误认为自动建表                      | “模式有主”           | *“Syntax: create schema [ SchemaName ] [ [ authorization ] Authorization ] { SchemaElementDefinition }”*                                    |      |          |
| 12 | Table 定义                       | 列 + 约束                             | 混约束与类型                       | “列 + 约”          | *“An SQL table consists of an ordered set of attributes and a (possibly empty) set of constraints”*                                         |      |          |
| 13 | Attribute 声明                   | 列定义语法 + 默认值 + 约束                   | 顺序写错                         | “名型默限”           | *“AttributeName Domain [ DefaultValue ] [ Constraints ]”*                                                                                   |      |          |
| 14 | PRIMARY / UNIQUE               | 主键唯一非空，UNIQUE 可多列                  | 把 UNIQUE 等同 PK               | “主不空，唯可空”        | *“primary key … unique( Surname, FirstName )”*                                                                                              |      |          |
| 15 | FOREIGN KEY                    | 外键指向唯一列                            | 指向非唯一列错误                     | “外键找唯一朋友”        | *“references Department(DeptName) on delete set null on update cascade”*                                                                    |      |          |
| 16 | Reaction Policies              | on delete / update 规则              | 忘记默认 NO ACTION               | “删改四兄弟”          | *“on delete set null on update cascade”*                                                                                                    |      |          |
| 17 | CHECK 约束                       | 检查列值条件                             | 不能跨表                         | “CHECK 只能管自己表”   | 出版课件未给 CHECK 跨表原文句子，但有提到“check described later”                                                                                             |      |          |
| 18 | NOT NULL                       | 列值不可为 NULL                         | 误以为全列都非空                     | “不写就能空”          | *“character(20) not null”*（在 Table 示例中）                                                                                                     |      |          |
| 19 | UNIQUE 约束                      | 列必须唯一，可组合                          | 写错只有单列                       | “独一但可空”          | *“unique( Surname, FirstName )”*                                                                                                            |      |          |
| 20 | DEFAULT + NULL                 | default null 与 NOT NULL 区别         | 混为一体                         | “空是态度，默是选项”      | *“default < GenericValue                                                                                                                    | user | null >”* |
| 21 | Derived Operations             | JOIN, INTERSECTION, RENAME         | 把 PROJECTION 当派生             | “拼出来的才叫派生”       | *“Derived operation: Join … Intersection … Renaming”*                                                                                       |      |          |
| 22 | Semantic Integrity             | 合理逻辑约束                             | 把结构约束归入                      | “语义 = 数据的道理”     | *“A constraint is a property that a set of data must satisfy.”*                                                                             |      |          |
| 23 | Attribute Constraints          | 单列约束                               | 写多列错                         | “一列一规则”          | *“on a single tuple: attribute constraints”*                                                                                                |      |          |
| 24 | Multiple Attribute Constraints | 同行多列比较                             | 写聚合或跨行错                      | “行内多对比”          | *“on a single relation … multiple attribute constraints”*                                                                                   |      |          |
| 25 | Functional Dependencies        | X→Y 关系                             | 当做 SQL check                 | “谁决定谁”           | *“on multiple tuples of the same relation: functional dependencies”*                                                                        |      |          |
| 26 | Cardinality Constraints        | 限制数量                               | 与聚合混淆                        | “数人头”            | *“there must be at least 3 technicians (i.e., 3 employees whose job = “technician”)”*                                                       |      |          |
| 27 | Aggregation Constraints        | SUM / AVG 约束                       | 误写成普通 CHECK                  | “算总数的约束”         | *“the average salary for a technician must be greater than 500”*                                                                            |      |          |
| 28 | Referential Integrity          | 外键引用主表存在性                          | 指向非唯一表错误                     | “找得到爹”           | *“If a tuple t references v1,…,vn as values of a foreign key, there must be a tuple t’ in the referenced relation with key values v1,…,vn”* |      |          |
| 29 | Immediate / Deferred           | 即时或延迟检查约束                          | 混淆什么时候检查                     | “即时查，延迟放”        | *“constraints can be immediate … or deferred … verified only at the end of a series of operations”*                                         |      |          |
| 30 | Schema vs Instance             | Schema 是结构，Instance 是数据            | 混为一体                         | “表是骨，数据是肉”       | 课件中没有一句明确原文提到这个对比但在 context “schema definition” 部分隐含区分。                                                                                     |      |          |

---



### 🎯 四、语义约束的区别

| 约束类型                          | 限制对象          | 示例                             | 关键点    |
| ----------------------------- | ------------- | ------------------------------ | ------ |
| Attribute constraint          | 单个属性值         | `Salary >= 500`                | 针对单列   |
| Multiple attribute constraint | 同行多列          | `Bonus < Salary`               | 同一个元组  |
| Functional dependency         | 不同行之间         | `DeptID → Manager`             | 跨元组关系  |
| **Cardinality constraint**    | **满足条件的元组数量** | `COUNT(Job='Technician') >= 3` | 跨元组数量级 |
| Aggregation constraint        | 聚合统计结果        | `AVG(Salary) < 5000`           | 数值统计   |
|

---

---

### 🧾 SQL Part 2 知识点对照表（完整版）

| 💡 知识点                                        | 📘 常考内容 / 题型提示                                      | 🧠 解题技巧与辨析                                                      | 📄 PPT 原文句子                                                                                         |                  |          |             |                                    |            |
| --------------------------------------------- | --------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ---------------- | -------- | ----------- | ---------------------------------- | ---------- |
| **Constraints（约束）**                           | “什么是 constraint”、“哪些语句可定义约束”                        | 所有约束都是条件，必须在每个数据库实例中成立                                          | *“Constraints are conditions that must be verified by every database instance.”*                    |                  |          |             |                                    |            |
| **Intra-relational constraints**              | 属于单表约束类型题。考点常问：“哪项属于intra-relational constraint？”   | 关键字：`NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `CHECK`（在单表内）          | *“Intra-relational constraints involve a single relation.”*                                         |                  |          |             |                                    |            |
| **Inter-relational constraints**              | 跨表约束题。常考：“哪种约束涉及多个关系？”、“referential integrity属于哪种？” | 关键字：`FOREIGN KEY`, `REFERENCES`, `ON DELETE / ON UPDATE`        | *“Constraints may take involve several relations.”*                                                 |                  |          |             |                                    |            |
| **NOT NULL**                                  | 单属性约束；常与`PRIMARY KEY`一起考。                           | 限制该属性不能为NULL；PK隐含NOT NULL                                       | *“not null (on single attributes)”*                                                                 |                  |          |             |                                    |            |
| **UNIQUE**                                    | 常考单属性vs多属性unique区别                                  | 单属性：写在域后；多属性：`unique(attr1, attr2)`                             | *“unique: permits the definition of keys; for multiple attributes: unique(Attribute{, Attribute})”* |                  |          |             |                                    |            |
| **PRIMARY KEY**                               | 考点：每个表最多一个主键；隐含`NOT NULL`和`UNIQUE`                  | 答题技巧：主键可多列组成，但只有一个PK定义                                          | *“primary key: defines the primary key (once for each table; implies not null)”*                    |                  |          |             |                                    |            |
| **CHECK (单表内)**                               | 考题常见：“check可用于单表或多表？”                               | 在intra中仅单表；在inter中可跨表                                           | *“check: described later”*                                                                          |                  |          |             |                                    |            |
| **REFERENCES / FOREIGN KEY**                  | 考题：如何定义外键，涉及referential integrity                   | 单属性：`references`；多属性：`foreign key(...) references ...`          | *“references and foreign key permit the definition of referential integrity constraints.”*          |                  |          |             |                                    |            |
| **Referential Integrity Constraint（参照完整性约束）** | 高频考点：对外键引用约束的违反与反应策略                                | 涉及两个表：一个含外键，一个被引用                                               | *“It is possible to associate reaction policies to violations of referential integrity.”*           |                  |          |             |                                    |            |
| **Reaction Policies**                         | 必考点。问“当外键引用的表被删除/更新时会怎样？”                           | 答题技巧：记4个动作关键词：`cascade`, `set null`, `set default`, `no action` | *“Reactions: – cascade – set null – set default – no action”*                                       |                  |          |             |                                    |            |
| **Cascade**                                   | 考法：`on delete cascade` / `on update cascade`        | 变化自动传播到子表                                                       | *“cascade: propagate the change”*                                                                   |                  |          |             |                                    |            |
| **Set Null**                                  | 考法：on delete时外键设为null                               | 子表引用值被置空                                                        | *“set null: nullify the referring attributes”*                                                      |                  |          |             |                                    |            |
| **Set Default**                               | 考法：设置默认值代替被删除值                                      | 外键列改为默认值                                                        | *“set default: assign the default value to the referring attributes”*                               |                  |          |             |                                    |            |
| **No Action / Restrict**                      | 常考混淆题                                               | 禁止修改或删除引用目标（SQL默认策略）                                            | *“no action (also: restrict): forbid the change on the external table.”*                            |                  |          |             |                                    |            |
| **on delete / on update**                     | 考法：语法层面和触发条件区分                                      | 两种事件触发不同反应策略                                                    | *“Reactions may depend on the event; syntax: on <delete                                             | update> <cascade | set null | set default | no action>”*                       |            |
| **Schema Updates**                            | 考法：DDL操作有哪些可改变结构                                    | 命令：`ALTER`, `DROP`（有时附 restrict / cascade）                      | *“Two SQL statements: alter (alter domain..., alter table…) – drop.”*                               |                  |          |             |                                    |            |
| **ALTER TABLE**                               | 考法：增删列语法                                            | 例：`alter table Department add column NoOfOffices integer`       | *“alter table Department add column NoOfOffices integer”*                                           |                  |          |             |                                    |            |
| **DROP**                                      | 考法：drop的作用对象与选项                                     | 可删除 schema / domain / table / view / assertion                  | *“drop <schema                                                                                      | domain           | table    | view        | assertion> ComponentName [restrict | cascade]”* |
| **DROP RESTRICT vs CASCADE**                  | 考法：区别 restrict / cascade 行为                         | restrict：若被依赖则禁止删除；cascade：连同依赖对象删除                             | *“drop ... [restrict                                                                                | cascade]”*       |          |             |                                    |            |
| **Inter-relational CHECK（多表check）**           | 进阶题                                                 | 可定义在schema或assertion级别                                          | *“check: described later”*（在后续assertion部分详细）                                                        |                  |          |             |                                    |            |

---



---

## 🧩 一、当外键引用的表被删除/更新时，会怎样？

这个问题考的就是 **Referential Integrity（参照完整性约束）** 和 **Reaction Policies（反应策略）**。

### 📖 背景：

我们有两张表：

```sql
Department(DeptName PRIMARY KEY)
Employee(RegNo PRIMARY KEY, Dept REFERENCES Department(DeptName))
```

Employee 表中的 `Dept` 是外键，**引用** Department 表的主键 `DeptName`。

---

### 🧨 当被引用的表（Department）被修改时：

#### 情况 1️⃣：更新 DeptName

比如原来 DeptName = 'IT'，现在改成 'Tech'。

#### 情况 2️⃣：删除 DeptName

比如删除了 'IT' 这一行。

---

这时 Employee 表里的外键 `Dept='IT'` 就**找不到对应对象**了，
如果不处理，就会破坏 referential integrity（参照完整性）。

所以 SQL 给出 **4种反应策略（Reaction Policies）**：

| 策略                         | 关键字                                       | 含义                                                                 |
| -------------------------- | ----------------------------------------- | ------------------------------------------------------------------ |
| ① **CASCADE**              | `ON DELETE CASCADE` / `ON UPDATE CASCADE` | 外键表（Employee）随之改变。删除 Dept → 删除该部门的所有员工。更新 DeptName → 同步更新员工的 Dept。 |
| ② **SET NULL**             | `ON DELETE SET NULL`                      | 删除主表时，把外键表对应列设为 NULL。                                              |
| ③ **SET DEFAULT**          | `ON DELETE SET DEFAULT`                   | 删除主表时，把外键列设为默认值。                                                   |
| ④ **NO ACTION（或RESTRICT）** | `ON DELETE NO ACTION`                     | 阻止删除或更新操作。主表有被引用就不能改。                                              |

---

### 📜 举例：

```sql
create table Employee (
  RegNo char(6) primary key,
  Dept char(15)
    references Department(DeptName)
    on delete set null
    on update cascade
);
```

* 如果删除一个部门：
  那个部门的所有员工 Dept → 变成 `NULL`
* 如果更新部门名字：
  员工的 Dept 同步修改

---

### 📘 PPT 原句：

> “Reactions operate on the table containing the foreign key, after changes to the external (referenced) table.”
> “Reactions may depend on the event; syntax: on <delete | update> <cascade | set null | set default | no action>”

意思是👇

* **这些反应操作发生在含外键的表（Employee）上**；
* **触发条件（event）可以是主表的 delete 或 update**；
* **你可以为每种事件单独指定不同的反应策略**。

例如：

```sql
on delete set null
on update cascade
```

---

## 🧩 二、DDL 和 DML 操作有哪些可以改变结构？

### 🧱 1️⃣ DDL（Data Definition Language）数据定义语言

📚 用来**定义或修改数据库结构（schema）**，比如表、列、索引、视图等。

| 操作         | 功能             | 是否改变结构  |
| ---------- | -------------- | ------- |
| `CREATE`   | 新建表、视图、域等      | ✅       |
| `ALTER`    | 修改已有表或域结构      | ✅       |
| `DROP`     | 删除表、视图、域等      | ✅       |
| `TRUNCATE` | 删除表中所有数据，但结构保留 | ❌（保留结构） |

PPT 原句：

> “Two SQL statements: alter (alter domain ..., alter table …) – drop.”

---

### 🧰 2️⃣ DML（Data Manipulation Language）数据操作语言

📚 用来**操作表中数据内容**，而不是结构。

| 操作       | 功能    | 是否改变结构 |
| -------- | ----- | ------ |
| `INSERT` | 插入数据行 | ❌      |
| `UPDATE` | 更新数据行 | ❌      |
| `DELETE` | 删除数据行 | ❌      |
| `SELECT` | 查询数据  | ❌      |

PPT 没直接写 DML，但前面 Part1 提到过：

> “SQL is both a DDL and a DML.”

---

### 🧩 结构变化总结：

| 分类  | 操作     | 是否改变结构 | 示例                              |
| --- | ------ | ------ | ------------------------------- |
| DDL | CREATE | ✅      | create table Student (...)      |
| DDL | ALTER  | ✅      | alter table add column Age int  |
| DDL | DROP   | ✅      | drop table Student cascade      |
| DML | INSERT | ❌      | insert into Student values(...) |
| DML | UPDATE | ❌      | update Student set ...          |
| DML | DELETE | ❌      | delete from Student where ...   |

---




## 🧭 前三章 全知识点速查表

| 知识点名称                               | 定义与解释                                                                                | 举例 / 延伸说明                                         | PPT 原句                                                                                       |              |
| ----------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------ |
| **Data Model**                      | 描述和组织数据及其关系的一组概念与结构。用于数据库设计的抽象层。                                                     | E-R 模型是概念层；Relational 模型是逻辑层。                     | “Set of concepts and constructs used to describe and organize data and their relationships.” |              |
| **Conceptual Schema**               | 描述数据库逻辑结构的模式，包括对象类型、关系、约束。                                                           | 例如，定义 `EMPLOYEE` 实体、属性和约束。                        | “The schema describes the structure of the data and the constraints on it.”                  |              |
| **Instance**                        | 某一时刻数据库中数据的实际状态。                                                                     | 表中当前的记录集合。                                        | “The data in the database at a particular moment in time is called an instance.”             |              |
| **Database Schema vs Instance**     | Schema 是结构定义（静态），Instance 是当前数据（动态）。                                                 | Schema 不变，Instance 随数据变化。                         | “Schema – structure definition; Instance – current content.”                                 |              |
| **Relational Model**                | 用表格（relation）来组织数据，每行是元组，每列是属性。                                                      | 一张表代表一个关系。                                        | “Data is represented as a collection of relations (tables).”                                 |              |
| **Relation**                        | 一个由属性（列）和元组（行）组成的集合。                                                                 | 类似 Excel 表。                                       | “A relation can be represented as a table.”                                                  |              |
| **Attribute**                       | 表中的列，描述关系的一个特征。                                                                      | EMPLOYEE(Name, Salary)。                           | “Each column of a relation corresponds to an attribute.”                                     |              |
| **Tuple**                           | 表中的一行，表示一个对象或实体的实例。                                                                  | 一名员工的信息。                                          | “Each row (tuple) in the table represents a single entity instance.”                         |              |
| **Domain**                          | 属性可取的合法值的集合。                                                                         | 性别域 = {‘M’, ‘F’}。                                 | “The domain of an attribute is the set of allowed values for that attribute.”                |              |
| **Degree**                          | 关系中属性（列）的数量。                                                                         | EMPLOYEE(EmpID, Name, Salary) → degree=3。         | “The degree of a relation is the number of attributes (columns).”                            |              |
| **Cardinality**                     | 关系中元组（行）的数量。                                                                         | EMPLOYEE 表有 10 行 → cardinality=10。                | “The cardinality of a relation is the number of tuples (rows).”                              |              |
| **Primary Key**                     | 唯一标识每个元组的属性集，不允许为空。                                                                  | EmpID。                                            | “Primary key uniquely identifies each tuple of a relation.”                                  |              |
| **Candidate Key**                   | 能唯一标识元组的属性集合中，任意一个都可能成为主键。                                                           | EmpID 或 (Name, BirthDate)。                        | “A candidate key is a minimal set of attributes that uniquely identifies tuples.”            |              |
| **Foreign Key**                     | 一个关系中用于引用另一个关系主键的属性。                                                                 | EMPLOYEE.DeptID → DEPARTMENT.DeptID。              | “A foreign key establishes a link between tuples of two relations.”                          |              |
| **Referential Integrity**           | 外键引用必须在被引用表中存在。                                                                      | 若 DeptID=10 不存在于 DEPARTMENTS 中则违规。                | “If a tuple t references v1,…,vn as foreign key values, there must be a tuple t’…”           |              |
| **Reactions to Violations**         | 当被引用表更新或删除时，引用方需反应。                                                                  | 可设为 `ON DELETE CASCADE`、`SET NULL`、`NO ACTION` 等。 | “Reactions may depend on the event; syntax: ON <DELETE                                       | UPDATE> ...” |
| **Semantic Integrity Constraints**  | 数据必须满足的语义性条件，确保现实世界意义正确。                                                             | Salary ≥ 500；DeptID 必须存在；Bonus < Salary。          | “A constraint is a property that a set of data must satisfy.”                                |              |
| **Types of Constraints**            | ① Domain constraint ② Key constraint ③ Referential constraint ④ Semantic constraint。 | 语义约束最灵活，例如 CHECK 条件。                              | “Constraints can be classified into domain, key, referential, and semantic.”                 |              |
| **CHECK Constraint**                | 限制属性或元组取值范围，可跨多属性定义。                                                                 | CHECK(Salary > Bonus)。                            | “CHECK constraints can be defined on one or more attributes.”                                |              |
| **Inter-relational Conditions**     | 跨表的语义约束，用于表达表之间的逻辑关系。                                                                | 员工工资总和 ≤ 部门预算。                                    | “Constraints may involve multiple relations.”                                                |              |
| **DDL（Data Definition Language）**   | 定义和修改数据库结构的 SQL 部分。                                                                  | CREATE, ALTER, DROP。                              | “DDL statements define or modify database schema elements.”                                  |              |
| **DML（Data Manipulation Language）** | 操作数据内容的 SQL 部分。                                                                      | SELECT, INSERT, UPDATE, DELETE。                   | “DML statements are used to query and update data.”                                          |              |
| **Relational Algebra**              | 一种操作关系型数据的形式化语言，SQL 的理论基础。                                                           | 结果总是一个关系（封闭性）。                                    | “Relational algebra is a procedural query language.”                                         |              |
| **Five Basic Operations**           | Selection (σ), Projection (π), Union (∪), Difference (−), Cartesian Product (×)。     | 基础操作足以表达所有查询。                                     | “These five operations are fundamental.”                                                     |              |
| **Derived Operations**              | 由基本操作组合得到：Join, Intersection, Division, Rename。                                      | Join = σ(condition)(R × S)。                       | “Derived operations are built from basic ones.”                                              |              |
| **Join（连接）**                        | 根据条件将两个关系的元组合并。                                                                      | R ⋈ S。                                            | “Join combines tuples from two relations based on a condition.”                              |              |
| **Natural Join**                    | 自动按同名属性连接并去除重复列。                                                                     | EMP ⋈ DEPT。                                       | “If we omit the predicate, the join is based on equality of all common attributes.”          |              |
| **Theta Join**                      | 使用一般条件（<, >, =, ≤, ≥, ≠）连接。                                                          | R ⋈(R.A < S.B) S。                                 | “A theta join uses a comparison operator in the join condition.”                             |              |
| **Equi-Join**                       | 连接条件仅使用 “=”。                                                                         | R ⋈(R.ID = S.ID) S。                               | “Equi-join is a theta join with equality condition only.”                                    |              |
| **Intersection**                    | 返回两个关系共有的元组。                                                                         | R ∩ S。                                            | “Intersection returns tuples that appear in both relations.”                                 |              |
| **Division**                        | 找出与另一关系所有值匹配的元组。                                                                     | “Find employees who worked on all projects.”      | “Division operator identifies tuples associated with all tuples of another relation.”        |              |
| **Rename (ρ)**                      | 重命名属性或关系。                                                                            | ρ(NewName)(R)。                                    | “Rename changes the name of relation or attributes.”                                         |              |
| **Closure Property**                | 所有关系代数操作结果仍是关系。                                                                      | σ(π(R)) 仍是一个关系。                                   | “Relational algebra is closed under its operations.”                                         |              |
| **Cardinality Constraint**          | 限定实体间关系数量（min,max）。                                                                  | 员工与部门关系 (1,N)。                                    | “Cardinality constraint indicates the minimum and maximum number of occurrences.”            |              |

---

## 📘 小结 — 高频考点 / 做题技巧

| 知识点                             | 常见题型        | 答题技巧                                                   |
| ------------------------------- | ----------- | ------------------------------------------------------ |
| SQL 定义与功能                       | 单选、填空       | “Structured Query Language” 不只定义数据（DDL），也能操作（DML）。     |
| Relation, Attribute, Tuple      | 概念题         | 记住：行=tuple，列=attribute。                                |
| Key vs Foreign Key              | 约束题         | 外键不能引用不存在的主键。                                          |
| Referential Integrity Reactions | 场景题         | 删除/更新时影响依赖表：cascade, set null, set default, no action。 |
| Derived Operations              | 理论题         | 只有 Join, Intersection, Division, Rename 属于 derived。    |
| Semantic Constraints            | 判断题         | 可以跨多属性、多表定义。                                           |
| CHECK                           | 语法题         | 可用于多属性约束，不限于单列。                                        |
| DDL / DML                       | 分类题         | 结构类 vs 数据类。                                            |
| Join 类型                         | SQL / 代数混合题 | 自然连接 = 交集条件连接 + 去重。                                    |
| Cardinality Constraint          | E-R 模型题     | 一般为 (min, max) 两个数，如 (0, N) 或 (1, 1)。                  |

---
