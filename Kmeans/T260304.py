import sys
import numpy as np


def solve():
    data  = sys.stdin.read().strip().split()

    if not data:
        return

    idx = 0

    k  = int(data[idx])
    idx += 1

    centers = []
    for _ in range(k):
        x = float(data[idx])
        y = float(data[idx + 1])
        z = float(data[idx + 2])
        centers.append([x, y, z])
        idx += 3
    centers = np.array(centers, dtype = float)

    t = int(data[idx]) # 迭代数
    idx += 1

    m = int(data[idx]) # 样本数
    idx +=1

    samples = []
    for _ in range(m):
        x = float(data[idx])
        y = float(data[idx + 1])
        z = float(data[idx + 2])
        samples.append([x, y, z])
        idx += 3
    samples = np.array(samples,dtype = float)

    for _ in range(t):
        # 1.分配
        # samples.shape = (m,3)
        # centers.shape = (k,3)
        distances = np.sqrt(np.sum((samples[:, np.newaxis, :] - centers[np.newaxis, :, :]) ** 2, axis=2))

        # 2.将每个样本分配给最近的中心
        labels = np.argmin(distances, axis = 1)

        # 3.更新中心点
        new_centers = centers.copy()
        for i in range(k):
            cluster_points = samples[labels == i]
            if len(cluster_points) > 0:
                new_centers[i] = np.mean(cluster_points,axis=0)

        centers = new_centers

    for center in centers:
        print(f'{center[0]:.2f} {center[1]:.2f} {center[2]:.2f}')

if __name__ == '__main__':
    solve()
