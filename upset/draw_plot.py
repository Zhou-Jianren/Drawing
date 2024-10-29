import itertools
import numpy as np
import pandas as pd
from matplotlib import rcParams
from matplotlib import pyplot as plt
import matplotlib.font_manager as fm
from upsetplot import from_indicators, plot
from matplotlib import pyplot as plt, rcParams


excel_path=f'F:/Zero/MFBP/draw/data/upset_test.xlsx'
df=pd.read_excel(excel_path)

df=df.astype(bool)

# 重新加载 matplotlib 配置
plt.rcdefaults()

# 设置全局字体
font = {'family': 'Times New Roman', 'size': 12}
plt.rc('font',family='Times New Roman')

# 设置画布大小
fig = plt.figure(figsize=(10, 6))

plot_result = plot(from_indicators(df), subset_size='count',  facecolor="black",
                   show_counts=True, sort_by='cardinality', max_subset_rank=10,
                   fig=fig, element_size=None, intersection_plot_elements=11, totals_plot_elements=3)

# 调整图形内容
plot_result["intersections"].set_ylabel("Intersection size")
plot_result["totals"].set_xlabel("Category Size")
plot_result["intersections"].set_yticks(np.arange(0, 501, 100))    # 纵坐标上下界、步长调整
plot_result["totals"].set_xticks(np.arange(0, 501, 100))   # 横坐标上下界、步长调整

# 只绘制 y=0 的网格线
plot_result["intersections"].grid(False)  # 关闭 y 轴主刻度的网格线
plot_result["intersections"].axhline(y=-0.12, color='black', linewidth=1)  # 手动绘制 y=0 的线

plot_result["totals"].grid(False)

plt.savefig("F:/Zero/MFBP/draw/image/upset_test.png", dpi=300, format="png")

# plt.show()
