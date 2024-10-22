import numpy as np
from math import pi
import pandas as pd
import matplotlib.pyplot as plt


# 假设 Excel 文件的格式如下：
# | Model       | Precision | Accuracy | Absolute True | Coverage |
# |-------------|-----------|----------|---------------|----------|
# | CNN         | 0.75      | 0.70     | 0.43          | 0.50     |
# | CNN with GAT| 0.65      | 0.80     | 0.55          | 0.46     |

# 读取 Excel 文件
excel_path = 'F:/Zero/MFBP/draw/data/Data.xlsx'
sheet_name = 'feature'
df = pd.read_excel(excel_path, sheet_name=sheet_name)

# 提取标签
labels = df.columns[1:].tolist()
n = len(labels)

# 对较长的标签进行换行处理
labels = [label.replace(' ', '\n') for label in labels]

# 提取数据
data = df.set_index('Features').T.to_dict('list')

# 为每个模型的数据添加第一个值到末尾，以闭合雷达图
for model in data:
    data[model] += data[model][:1]

# 计算角度
angles = [i / float(n) * 2 * pi for i in range(n)]
angles += angles[:1]

# 设置全局字体
plt.rcParams['font.family'] = 'Times New Roman'  # 设置字体为 SimHei（黑体）
plt.rcParams['font.size'] = 12  # 设置全局字体大小

fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))


# 设置 y 轴的范围
ax.set_ylim(0.05, 0.92)
# 设置 y 轴刻度的间隔
ax.set_yticks([0.05, 0.2, 0.4, 0.6, 0.8, 0.92])
ax.set_yticklabels([])  # 隐藏 y 轴刻度值

# 定义颜色列表
colors = ['#FFBC80', '#6B98C4', '#B4DEA2']

# 绘制每个模型的数据
for i, (model, values) in enumerate(data.items()):
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=model, color=colors[i % len(colors)])
    ax.fill(angles, values, alpha=0.1, color=colors[i % len(colors)])

# 添加标签
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=16)
ax.xaxis.set_tick_params(pad=20)  # 增加标签和图形的距离

# 调整图例字体大小
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

plt.savefig("F:/Zero/MFBP/draw/image/radar.png", dpi=300, format="png")

# plt.show()
