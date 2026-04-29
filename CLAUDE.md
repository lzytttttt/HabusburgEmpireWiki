# 项目规则

## 项目目标

将玛玛吉《哈布斯堡帝国的崛起》中译初稿整理为 Markdown wiki，在 wiki 化过程中完成校对、术语统一、人物索引、地名索引、时间线和待考问题整理。

## 文件结构

- `manuscript/original/` — 原始文稿，**禁止修改**
- `manuscript/working/` — 工作副本，校对整理在此进行
- `wiki/` — Markdown wiki 输出
- `wiki/chapters/` — 按章节拆分的 wiki 页面
- `notes/` — 工作笔记、校对规则、待考问题
- `data/` — 结构化数据
- `scripts/` — 自动化脚本

## 禁止规则

- **禁止修改 `manuscript/original/` 中的任何文件**
- **禁止直接覆盖原始文稿**
- **禁止在未确认的情况下删除任何文件**

## 校对原则

- 校对在 `manuscript/working/` 中进行
- 不改动原意，只修正明显的错别字、标点、格式问题
- 术语统一以 `notes/style-guide.md` 为准
- 所有不确定之处标记为 `TODO` 并记录到 `notes/unresolved.md`

## Wiki 页面规则

- 每个章节对应 `wiki/chapters/` 下的一个文件
- 使用 `[[页面名]]` 格式进行内部链接
- 术语首次出现时加粗并链接到术语表
- 人物首次出现时链接到人物索引

## 标记规范

- `TODO` — 待处理事项
- `REVIEW` — 需要人工复核
- `TERM` — 术语，需统一
- `NOTE` — 备注说明

## 工作方式

- 每次只处理一个章节
- 完成一个章节后更新 `wiki/Editorial-Log.md`
- 不做超出当前章节范围的修改
