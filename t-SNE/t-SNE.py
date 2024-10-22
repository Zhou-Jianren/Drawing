import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE


# 假设你的特征和标签数据
features = np.load('F:/Zero/MFBP/dataset/MFBP/test/robert.npy')
labels = np.load('F:/Zero/MFBP/dataset/MFBP/test/label.npy')  # shape: (样本数, 5)

# 进行t-SNE降维
tsne = TSNE(n_components=2, random_state=42)
features_tsne = tsne.fit_transform(features)

# 创建一个标签组合的列表
label_combinations = [''.join(map(str, row)) for row in labels]
# print(label_combinations)

# 设置全局字体
plt.rcParams['font.family'] = 'Times New Roman'  # 设置字体
plt.rcParams['font.size'] = 12  # 设置全局字体大小

# 使用不同的颜色绘制每种组合
# unique_combinations = sorted(list(set(label_combinations)))     # 使用 sorted() 保证排序顺序

# 手动定义标签组合的顺序
unique_combinations = ['01000', '00100', '00010', '00001', '10000', '00101', '00110', '11000']

# 为每个图例添加名称和颜色
combination_names = {
    '10000': 'AMP',
    '01000': 'ACP',
    '00100': 'ADP',
    '00010': 'AHP',
    '00001': 'AIP',
    '00101': 'ADP_AIP',
    '00110': 'ADP_AHP',
    '11000': 'AMP_ACP'
}

colors = ['#746fe5', '#0080eb', '#0088db', '#008bb9', '#00898f', '#008464', '#484554', '#e04649']

plt.figure(figsize=(10, 6))

for i, combination in enumerate(unique_combinations):
    idx = np.where(np.array(label_combinations) == combination)[0]
    plt.scatter(features_tsne[idx, 0], features_tsne[idx, 1], 
                color=colors[i % len(colors)], 
                label=combination_names.get(combination, f'Combination {combination}'))

plt.title('RoBERTa T-SNE Visualization', fontsize=18)
plt.xlabel('T-SNE Component 1', fontsize=16)
plt.ylabel('T-SNE Component 2', fontsize=16)

# 调整图例的位置，放在图的外部右侧
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.savefig('F:/Zero/MFBP/draw/image/roberta.png', dpi=300, bbox_inches='tight')
# plt.show()
