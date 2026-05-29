# 哈布斯堡帝国的崛起 Wiki

基于玛玛吉（Mamatey, Victor S.）所著 *Rise of the Habsburg Empire, 1526-1851* 中译初稿整理而成的 Markdown wiki。

**在线访问：** [https://lzytttttt.github.io/HabusburgEmpireWiki](https://lzytttttt.github.io/HabusburgEmpireWiki)

## 关于本书

本书是一部关于哈布斯堡帝国（1526-1851）的历史著作，涵盖从莫哈奇之战到维也纳会议的三百年历史。原书以英文写成，本项目基于其中译初稿进行 wiki 化整理，旨在以结构化、可链接的方式呈现这段中欧历史。

## 特性

- **9 个章节** — 完整覆盖 1526-1815 年哈布斯堡帝国历史
- **180+ 人物索引** — 按历史时期分组，含人物关系
- **210+ 地名索引** — 按地理区域分组，标注现代名称
- **交互式时间线** — 基于 TimelineJS，146 个重大事件，支持缩放拖拽
- **Mermaid 关系图** — 家族世系图、战争因果图、改革措施图
- **历史疆域地图** — 1526、1648、1789 三个时期的 SVG 地图
- **术语表** — 制度法令、政治概念、宗教术语、军事术语

## Wiki 结构

### 章节（9 章）

| 章节 | 标题 | 时期 |
|------|------|------|
| [第1章](wiki/chapters/ch01-austria-and-habsburg.md) | 奥地利和哈布斯堡家族 | 起源-1526 |
| [第2章](wiki/chapters/ch02-bohemia.md) | 波西米亚 | 6世纪-1437 |
| [第3章](wiki/chapters/ch03-hungary.md) | 匈牙利 | 9世纪-1526 |
| [第4章](wiki/chapters/ch04-formation-of-habsburg-empire.md) | 哈布斯堡帝国的形成 | 1526-1648 |
| [第5章](wiki/chapters/ch05-thirty-years-war.md) | 三十年战争 | 1618-1648 |
| [第6章](wiki/chapters/ch06-consolidation-and-expansion.md) | 巩固和扩张 | 1648-1739 |
| [第7章](wiki/chapters/ch07-enlightened-absolutism.md) | 开明专制 | 1740-1789 |
| [第8章](wiki/chapters/ch08-empire-in-reform.md) | 改革中的帝国 | 1780-1792 |
| [第9章](wiki/chapters/ch09-revolution-and-napoleon.md) | 大革命与拿破仑 | 1792-1815 |

### 索引与专题页面

- **[人物索引](wiki/People.md)** — 按历史时期分组，收录 180+ 位历史人物
- **[地名索引](wiki/Places.md)** — 按地理区域分组，收录 210+ 个地名
- **[术语表](wiki/Glossary.md)** — 制度法令、政治概念、宗教术语、军事术语
- **[时间线](wiki/Timeline.md)** — 重大事件按时间排序，标记战争/改革/外交/宗教主题
- **[交互式时间线](wiki/timeline-interactive.md)** — TimelineJS 呈现，支持缩放拖拽
- **[哈布斯堡家族世系表](wiki/Habsburg-Genealogy.md)** — Mermaid 世系图 + 家族联姻与格言
- **[战争列表](wiki/Wars.md)** — 约 40 场战争与战役
- **[条约列表](wiki/Treaties.md)** — 约 40 项条约与和约

### 其他

- **[待考问题](wiki/Open-Questions.md)** — 校对中发现的存疑之处
- **[校订日志](wiki/Editorial-Log.md)** — 整理工作记录

## 技术栈

- **MkDocs Material** — 静态站点生成器，中文语言支持
- **TimelineJS v3** — 交互式时间线
- **Mermaid.js** — 关系图/流程图
- **GitHub Pages** — 自动部署（GitHub Actions）

## 文件结构

```
wiki/                   ← Markdown wiki 主目录
  chapters/             ← 9 个章节页面
  assets/
    images/             ← 历史人物 SVG 占位图（15 张）
    maps/               ← 疆域变化 SVG 地图（3 张）
    timeline/           ← TimelineJS JSON 数据
  stylesheets/          ← 自定义 CSS
  Home.md               ← Wiki 首页
  People.md             ← 人物索引
  Places.md             ← 地名索引
  Timeline.md           ← 时间线
  Glossary.md           ← 术语表
  Habsburg-Genealogy.md ← 哈布斯堡家族世系表
  Wars.md               ← 战争列表
  Treaties.md           ← 条约列表
  Open-Questions.md     ← 待考问题
  Editorial-Log.md      ← 校订日志
mkdocs.yml              ← MkDocs 配置
scripts/                ← 自动化脚本
notes/                  ← 工作笔记、校对规则
```

## 本地运行

```bash
pip install mkdocs-material
mkdocs serve
```

访问 http://127.0.0.1:8000 预览。

## 许可证

见 [LICENSE](LICENSE)。
