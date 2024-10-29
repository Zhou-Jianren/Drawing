import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def create_custom_bar_plot(df, title, y_min=None, y_max=None, save_path=None):
    labels = df.columns[1:]  # 提取数据框中的指标名称
    models = df.iloc[:, 0]   # 提取模型名称
    data = df.iloc[:, 1:].values  # 提取每个模型的数据
    
    x = np.arange(len(labels))  # 设置x轴上指标的位置
    width = 0.25  # 条形的宽度

    # 设置全局字体
    plt.rcParams['font.family'] = 'Times New Roman'  # 设置字体
    plt.rcParams['font.size'] = 12  # 设置全局字体大小

    fig, ax = plt.subplots(figsize=(10, 6))

    # 定义颜色
    colors = ['#f28e2c', '#4e79a7', '#e15759', '#76b7b2', '#59a14f', '#edc949', '#9998FF', '#9193B4', '#BABABA']
    
    # 使用自定义颜色绘制每个模型的数据
    for i, model in enumerate(models):
        ax.bar(x + i * width, data[i], width, label=model, color=colors[i % len(colors)])

    # 设置轴标签、标题和刻度
    # ax.set_xlabel('Metrics', fontsize=16)
    # ax.set_ylabel('Scores', fontsize=16)
    ax.set_title(title, fontsize=18)
    ax.set_xticks(x + width * (len(models) / 2 - 0.5))
    ax.set_xticklabels(labels, fontsize=14)

    # 设置y轴范围
    if y_min is not None and y_max is not None:
        ax.set_ylim(y_min, y_max)
    
    # 在每个条形上方添加数值
    # for i in range(len(models)):
    #     for j in range(len(labels)):
    #         ax.text(x[j] + i * width, data[i][j] + 0.01, f'{data[i][j]:.3f}', ha='center', va='bottom', fontsize=12, rotation=90)

    # 添加图例和布局调整
    # ax.legend(loc='upper left')
    plt.tight_layout()
    # 保存图像
    if save_path is not None:
        plt.savefig(save_path, dpi=300)
    # plt.show()

# Load the Excel file
file_path = 'F:/Zero/MFBP/draw/data/Data.xlsx'

# Read both sheets: ACE and ACP
data_bar = pd.read_excel(file_path, sheet_name='single_sp')

create_custom_bar_plot(data_bar, title="specificity(SPE)", y_min=0, y_max=1, save_path='draw/image/sp.png')
