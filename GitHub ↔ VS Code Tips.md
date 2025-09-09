---

# GitHub 与 VS Code 常用操作技巧

## 1️⃣ 打开仓库
- **前提**：已经在 GitHub 上创建仓库，并在本地 clone（或打开）到 VS Code。
- **步骤**：
  1. 在 VS Code 里点击 **File → Open Folder**。
  2. 选择你的仓库文件夹（例如 `6UIT-learning-journal`）。
- **提示**：确保文件夹里有 `.git` 文件夹，否则 VS Code 识别不了 Git 仓库。

## 2️⃣ 查看 Git 状态
```bash
git status
````

* 查看哪些文件被修改、哪些是未跟踪（Untracked）。

## 3️⃣ 添加修改到暂存区（Stage）

```bash
git add <文件名>
```

* 例如：

```bash
git add 2025-09-09.md
```

* **全部文件**：

```bash
git add .
```

## 4️⃣ 提交修改（Commit）

```bash
git commit -m "写你的本次修改说明"
```

* 示例：

```bash
git commit -m "更新 Web Development 2025/09/08 实时笔记"
```

## 5️⃣ 上传到 GitHub（Push）

```bash
git push
```

* 如果提示输入账号/密码，可以使用 GitHub Personal Access Token（PAT）替代密码。

## 6️⃣ 拉取 GitHub 上最新文件（Pull）

```bash
git pull
完全可以，这样非常高效！我帮你整理一份 **GitHub ↔ VS Code 常用操作技巧笔记**，用 Markdown 写好，你直接放到你的仓库里就行。你以后更新文件或打开最新内容可以直接参考，省去每次问我指令的麻烦。

---

````markdown
# GitHub 与 VS Code 常用操作技巧 / GitHub ↔ VS Code Tips

## 1️⃣ 打开仓库
- **前提**：已经在 GitHub 上创建仓库，并在本地 clone（或打开）到 VS Code。
- **步骤**：
  1. 在 VS Code 里点击 **File → Open Folder**。
  2. 选择你的仓库文件夹（例如 `6UIT-learning-journal`）。
- **提示**：确保文件夹里有 `.git` 文件夹，否则 VS Code 识别不了 Git 仓库。

## 2️⃣ 查看 Git 状态
```bash
git status
````

* 查看哪些文件被修改、哪些是未跟踪（Untracked）。

## 3️⃣ 添加修改到暂存区（Stage）

```bash
git add <文件名>
```

* 例如：

```bash
git add 2025-09-09.md
```

* **全部文件**：

```bash
git add .
```

## 4️⃣ 提交修改（Commit）

```bash
git commit -m "写你的本次修改说明"
```

* 示例：

```bash
git commit -m "更新 Web Development 2025/09/08 实时笔记"
```

## 5️⃣ 上传到 GitHub（Push）

```bash
git push
```

* 如果提示输入账号/密码，可以使用 GitHub Personal Access Token（PAT）替代密码。

## 6️⃣ 拉取 GitHub 上最新文件（Pull）

```bash
git pull
完全可以，这样非常高效！我帮你整理一份 GitHub ↔ VS Code 常用操作技巧笔记，用 Markdown 写好，你直接放到你的仓库里就行。你以后更新文件或打开最新内容可以直接参考，省去每次问我指令的麻烦。

# GitHub 与 VS Code 常用操作技巧 / GitHub ↔ VS Code Tips

## 1️⃣ 打开仓库
- **前提**：已经在 GitHub 上创建仓库，并在本地 clone（或打开）到 VS Code。
- **步骤**：
  1. 在 VS Code 里点击 **File → Open Folder**。
  2. 选择你的仓库文件夹（例如 `6UIT-learning-journal`）。
- **提示**：确保文件夹里有 `.git` 文件夹，否则 VS Code 识别不了 Git 仓库。

## 2️⃣ 查看 Git 状态
```bash
git status


查看哪些文件被修改、哪些是未跟踪（Untracked）。

3️⃣ 添加修改到暂存区（Stage）
git add <文件名>


例如：

git add 2025-09-09.md


全部文件：

git add .

4️⃣ 提交修改（Commit）
git commit -m "写你的本次修改说明"


示例：

git commit -m "更新 Web Development 2025/09/08 实时笔记"

5️⃣ 上传到 GitHub（Push）
git push


如果提示输入账号/密码，可以使用 GitHub Personal Access Token（PAT）替代密码。

6️⃣ 拉取 GitHub 上最新文件（Pull）
git pull


保证本地仓库与 GitHub 同步，尤其在多人协作或你在别的电脑更新过仓库时。

7️⃣ 查看历史版本（History）

在 VS Code 左侧 Source Control 或者右键文件选择 Open Timeline。

或在终端：

git log

8️⃣ 小技巧

Markdown 预览：Ctrl + Shift + V 或右键选择 Open Preview。

VS Code Git 面板：点击左侧 Source Control 图标，可以直接 stage/commit/push/pull，不用命令行。

保持文件后缀：Markdown 文件必须是 .md 才能渲染。

GitHub 文件夹与 VS Code 文件夹同步：

修改完本地文件 → git add → git commit → git push 上传。

GitHub 上有更新 → git pull 拉取到本地。
