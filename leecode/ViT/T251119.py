import sys
import numpy as np

def solve():
    data = list(map(int,input().split()))

    img_size = data[0]
    patch_size = data[1]
    channels = data[2]
    embedding_dim = data[3]

    n = img_size // patch_size # patch个数

    num_patch = n * n # 总的token数(patch数)

    # 每个patch展平后的维数
    patch_dim = patch_size * patch_size * channels

    # 线性映射后，patch嵌入
    patch_embedding = np.zeros((num_patch, embedding_dim), dtype=np.float32)

    cls_token = np.zeros((1, embedding_dim), dtype=np.float32)

    final_embedding = np.concatenate([cls_token,patch_embedding],axis = 0)

    print(final_embedding.shape[0], final_embedding.shape[1])

if __name__ == '__main__':
    solve()


