# VSCode 与 GitHub 操作小技巧

 1. 配置 Git
```bash
# 设置用户名和邮箱（只需设置一次）
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"

# 检查配置
git config --list

```

---

 2. 克隆仓库

```bash
git clone <仓库地址>
# 示例：
git clone https://github.com/username/repo.git
```

---

 3. VSCode 打开项目

1. 打开 VSCode → File → Open Folder → 选择仓库目录
2. 左侧 Source Control 面板显示修改状态

---

## 4. 常用 Git 命令

| 操作     | 命令                            | 说明                   |
| ------ | ----------------------------- | -------------------- |
| 查看状态   | `git status`                  | 显示修改文件状态             |
| 添加文件   | `git add <文件名>` 或 `git add .` | 将修改加入暂存区             |
| 提交修改   | `git commit -m "说明"`          | 提交到本地仓库              |
| 推送到远程  | `git push origin main`        | 上传到 GitHub (main 分支) |
| 拉取远程更新 | `git pull origin main`        | 同步远程仓库最新内容           |

---

 5. VSCode 内操作

| 操作    | 方法                                          |
| ----- | ------------------------------------------- |
| 提交修改  | Source Control → `+` 添加 → 输入提交信息 → √ Commit |
| 推送/拉取 | 左下角 `…` 菜单 → Pull / Push                    |
| 分支管理  | 左下角分支名 → 新建/切换分支                            |

---

## 6. 小技巧

* 每次修改前先 `git pull` 避免冲突
* VSCode 自动提示 Git 状态，非常直观
* 推荐安装插件 **GitLens** 查看历史和贡献者
* 常用快捷键：

  * `Ctrl + ~`：打开终端
  * `Ctrl + Shift + G`：打开 Source Control

---

## 7. 推荐流程

1. `git pull origin main` → 拉取远程更新
2. 修改/编辑文件
3. `git add .` → 添加修改
4. `git commit -m "说明"` → 提交
5. `git push origin main` → 上传到远程

