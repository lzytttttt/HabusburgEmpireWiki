# 交互式时间线

> 哈布斯堡帝国重大事件时间线（896-1815），基于 TimelineJS 呈现。

<div id="timeline-embed" style="width: 100%; height: 70vh; min-height: 400px;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var jsonPath = new URL('assets/timeline/timeline.json', window.location.href).href;
  fetch(jsonPath)
    .then(function(r) { return r.json(); })
    .then(function(data) {
      window.timeline = new TL.Timeline('timeline-embed', data, {
        hash_bookmark: true,
        start_at_end: false,
        default_bg_color: '#f5f5f5',
        scale_factor: 1,
        timenav_height: 200,
        marker_height_min: 30
      });
    })
    .catch(function(err) {
      document.getElementById('timeline-embed').innerHTML =
        '<p style="color:red;">加载时间线数据失败: ' + err.message + '</p>';
    });
});
</script>

## 主题图例

| 颜色 | 主题 |
|------|------|
| 🔴 红色 | 战争 |
| 🔵 蓝色 | 改革 |
| 🟢 绿色 | 外交 |
| 🟣 紫色 | 宗教 |

## 原始数据

完整的时间线文字数据请参见 [时间线](Timeline.md)。
