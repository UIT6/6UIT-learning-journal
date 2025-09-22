# 📝 Operating System 笔记整理（最新版）
[打开课件](https://github.com/UIT6/6UIT-learning-journal/blob/d8a8e6d921d3a93817699f626620b5d830dae982/Operating-System/course/file/01-%20Introduction%20to%20Operating%20Systems.pdf)
## 1️⃣ OS 定义（Operating System Definition）

- **没有统一定义**  
  - “Everything a vendor ships when you order an OS” → 你买的操作系统里厂商提供的全部内容
- **Kernel（内核）**：电脑里一直在运行的核心程序
- 其他部分：
  - **System Programs（系统程序）**：随 OS 提供
  - **Application Programs（应用程序）**：用户使用的软件

---

## 2️⃣ OS 的主要功能（What Operating Systems Do）

1. **Interface between user and hardware**  
   - OS 是**用户与硬件的接口**  

2. **Control interactions between users and programs**  
   - 控制用户和程序的交互，保证多用户、多程序安全运行  

3. **Provides a controlled and efficient environment for execution of programs**  
   - 提供**受控、高效的程序执行环境**  
Operating-System/course/notes
4. **Provides mechanisms (functionality) and policies (rules) to manage system resources**  
   - 提供机制 + 策略，管理系统资源  

---

## 3️⃣ 计算机系统四大组件（Four Components of a Computer System）

| Component | 内容 | 作用 |
|-----------|------|------|
| Hardware | CPU、Memory、I/O Device | 提供计算资源 |
| OS | 控制硬件，调度资源 | 资源管理、虚拟化、协调应用程序 |
| Application Program | 应用程序 | 利用系统资源完成任务 |
| User | 人或机器 | 提出需求、发出指令 |

💡 **比喻（最新版）**：
- 用户 = 老板
- 应用程序 = 项目经理 / 小经理
- OS = 工厂经理
- Kernel = 核心工人 / 执行者
- Hardware = 工厂机器
- Memory = 仓库
- System Bus = 运输通道
- VM / 小房间 = 被分配的独立工作环境

---

## 4️⃣ OS 的两种视角

### ① Virtual / Extended Machine View（虚拟机/扩展机视角）
- 用户视角（Top-down view）
- OS 提供理想化计算机环境，隐藏硬件低级细节
- 例子：虚拟机（VM）在 Windows 上运行 Linux，被 OS 分配一个隔离环境（小房间），Linux 觉得有独占资源

### ② Resource Manager View（资源管理者视角）
- 系统视角（Bottom-up view）
- OS 管理硬件资源：CPU、Memory、I/O Device
- 提供时间片和空间复用，保证多用户共享硬件
- Kernel 实际控制硬件执行操作

---

## 5️⃣ General Organization（计算机一般组织）

- **CPU、Device Controller 通过 System Bus 访问 Shared Memory**  
  - CPU = 工厂经理  
  - Device Controller = 各设备控制器（硬盘、USB、Graphics Adapter）  
  - System Bus = 工厂运输通道  
  - Shared Memory = 仓库（存储程序指令和数据）  
- 内存周期（Memory Cycle） = 内存完成一次读写操作的时间  
- CPU 和设备争抢内存周期时，OS/Kernel 协调  

---

## 6️⃣ 数据流（Data Movement）

- 数据在 CPU ↔ Memory ↔ Device 间流动
- **DMA（Direct Memory Access）**：设备直接搬数据，CPU 不干预，提高效率

---

## 7️⃣ 小比喻整合（最新版）

| 角色 | 类比 | 职责 |
|------|------|------|
| 用户 | 老板 | 提出需求或目标 |
| 应用程序 | 项目经理 / 小经理 | 把用户需求拆成任务，发给 OS，不自己操作硬件 |
| OS | 工厂经理 | 决策、调度、分配资源 |
| Kernel | 核心工人 / 执行者 | 直接操作硬件，实现 OS 策略 |
| Hardware | 工厂机器 | 真正完成任务 |
| Memory | 仓库 | 存储数据和指令 |
| System Bus | 运输通道 | CPU/设备搬运数据的通路 |
| VM / 小房间 | 独立工作环境 | 隔离资源，让应用觉得资源充足 |

---

# ❓ 疑问 Q&A 整理（最新版）

**Q1：OS 是怎么创造出来的？**  
- 因为早期程序员直接操作硬件太复杂、容易出错、无法高效多任务运行  
- OS 应运而生，统一管理资源、调度任务、提供接口  

**Q2：OS 是直接操作硬件吗？**  
- OS 内部的 **Kernel** 直接操作硬件  
- 应用程序不操作硬件，只发请求，Kernel 执行  

**Q3：应用程序是做什么的？**  
- 应用程序像项目经理，只负责把用户需求拆成任务  
- Kernel 才是实际操作硬件的人  

**Q4：OS 的鲁棒性是什么意思？**  
- 系统在异常或错误情况下仍能运行  
- 例如：一个程序崩溃了，其他程序和整个系统不受影响  

**Q5：虚拟机比喻怎么理解？**  
- OS 给每个应用或 VM 分配独立环境（小房间）  
- 房间是真实资源的一部分，但 OS 隔离和抽象，让应用觉得资源充足  

**Q6：CPU、Device Controller、Memory、System Bus 是什么？为什么要抢内存周期？**  
- CPU = 计算核心，Device Controller = 设备中介，Memory = 仓库  
- System Bus = 数据搬运通道  
- 内存一次只能处理一个读写请求，CPU 和设备需要排队 → OS/Kernel 协调  

**Q7：仓库存储的是什么？**  
- 内存储存程序指令和数据  
- 工厂设备（CPU/外设）需要这些数据执行任务  

**Q8：Data Movement 是什么？**  
- 数据在 CPU ↔ 内存 ↔ 设备之间流动  
- DMA = 设备直接搬数据，提高效率  

**Q9：Kernel 是什么？**  
- Kernel = 核心工人 / 执行者，直接操作硬件  
- 应用程序只发请求，不直接接触硬件  

**Q10：早期程序员直接操作硬件是怎样的？**  
- 使用 **打孔卡（punch card）** 或 **面板开关**  
- 写机器指令（LOAD, ADD, STORE 等），打孔卡顺序控制计算机  
- 既管理资源又执行任务，非常复杂且易出错  

