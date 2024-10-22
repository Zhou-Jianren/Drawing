import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def create_custom_polar_bar_plot(df, title, save_path=None):
    labels = df.columns[1:]  # 提取数据框中的指标名称
    models = df.iloc[:, 0]   # 提取模型名称
    data_1 = df.iloc[:, 1].values*100  # 提取每个模型的数据
    data_2 = df.iloc[:, 2].values*100  # 提取每个模型的数据
    data_3 = df.iloc[:, 3].values*100  # 提取每个模型的数据
    data_4 = df.iloc[:, 4].values*100  # 提取每个模型的数据
    # data_5 = df.iloc[:, 5].values*100  # 提取每个模型的数据
    data = [data_1, data_2, data_3, data_4]

    label_colors = ['#F39B7F', '#3C5488', '#00A087', '#4DBBD5', '#E64B35']

    # 画图
    fig = plt.figure(figsize=(4, 4), dpi=300, facecolor='white')
    ax = fig.add_subplot(projection='polar')
    
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    
    radii = [0]
    colors = ['white']
    for g, c in zip(data, label_colors):
        radii.extend(g-30)      # 控制数据最小值
        colors.extend([c]*len(g))
        radii.append(0)
        colors.append('white')
    radii.pop()
    colors.pop()
    
    N = len(radii)
    scale_lim = 50   # 比例尺的最大值
    scale_major = 10    # 刻度间隔
    bottom = 70      # 柱状图的底部高度
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    width = 2.5 * np.pi / (N + 9)
    
    # 画出柱状图
    ax.bar(theta, radii, width=width, bottom=bottom, color=colors)
    
    # 画出刻度
    def scale(ax, bottom, scale_lim, theta, width):
        t = np.linspace(theta-width/2, theta+width/2, 6)
        for i in range(int(bottom), int(bottom+scale_lim+scale_major), scale_major):
            ax.plot(t, [i]*6, linewidth=0.25, color='gray', alpha=0.8)
    
    # 画出刻度值
    def scale_value(ax, bottom, theta, scale_lim):
        for i in range(int(bottom), int(bottom+scale_lim+scale_major), scale_major):
            ax.text(theta,
                    i,
                    f'{i-bottom}',
                    fontsize=3,
                    alpha=0.8,
                    va='center',
                    ha='center'
                    )
    
    s_list = []
    g_no = 0
    for t, r in zip(theta, radii):
        if r == 0:
            s_list.append(t)
            if t == 0:
                # 添加刻度
                # scale_value(ax, bottom, t, scale_lim)
                # 隐藏刻度线
                scale(ax, bottom, scale_lim, t, width)
            else:
                scale(ax, bottom, scale_lim, t, width)
        else:
            t2 = np.rad2deg(t)
            # 标出每根柱的名称
            ax.text(t, r + bottom + scale_major*0.6,
                    models[g_no],
                    fontsize=6,
                    rotation=90-t2 if t < np.pi else 270-t2,
                    rotation_mode='anchor',
                    va='center',
                    ha='left' if t < np.pi else 'right',
                    color='black',
                    clip_on=False
                    )
            if g_no == (len(models)-1):
                g_no = 0
            else:
                g_no += 1
    
    
    s_list.append(2 * np.pi)
    
    for i in range(len(s_list)-1):
        t = np.linspace(s_list[i]+width, s_list[i+1]-width, 50)
        ax.plot(t, [bottom-scale_major*0.4]*50, linewidth=0.5, color='black')
        ax.text(s_list[i]+(s_list[i+1]-s_list[i])/2,
                bottom-scale_major*1.2,
                labels[i],
                va='center',
                ha='center',
                fontsize=7,
                )
    
    ax.set_rlim(30, bottom+scale_lim+scale_major)
    ax.axis('off')
    # plt.tight_layout()
    # 保存图像
    if save_path is not None:
        plt.savefig(save_path, dpi=300)
    
    plt.show()

# Load the Excel file
file_path = '数据表.xlsx'

# Read both sheets: ACE and ACP
ace_data = pd.read_excel(file_path, sheet_name='ACE_Method')
acp_data = pd.read_excel(file_path, sheet_name='ACP_Method')

# Custom plot for ACE and ACP data
# create_custom_polar_bar_plot(ace_data, title=None, save_path='graph/image/ACE_Method.jpeg')
create_custom_polar_bar_plot(acp_data, title=None, save_path='graph/image/ACP_Method.jpeg')
