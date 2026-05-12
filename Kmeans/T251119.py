def main():
    k, m, n = map(int, input().split())
    points = []
    for _ in range(m):
        point = list(map(float, input().split()))
        points.append(point)

    def solve():
        eps = 1e-8
        dim = 4
        # 初始质心统一采用给定数据集前 k 个点
        centers = []
        for i in range(k):
            centers.append(points[i][:])

        final_clusters = [[] for _ in range(k)]

        for _ in range(n):
            clusters = [[] for _ in range(k)]
            # 步骤 1：将每个点分配到距离最近的质心
            for point_index in range(m):
                point = points[point_index]
                best_center = 0
                best_distance = None

                for center_index in range(k):
                    center = centers[center_index]
                    distance = 0.0
                    # 计算欧氏距离的平方，比较大小时不需要开根号
                    for d in range(dim):
                        diff = point[d] - center[d]
                        distance += diff * diff

                    if best_distance is None:
                        best_distance = distance
                        best_center = center_index
                    else:
                        if distance < best_distance:
                            best_distance = distance
                            best_center = center_index

                clusters[best_center].append(point_index)
            # 步骤 2：根据每个簇内点的均值更新质心
            new_centers = []
            for center_index in range(k):
                cluster = clusters[center_index]
                # 题目说明默认每类终端都存在；这里仍保留空簇保护逻辑
                if len(cluster) == 0:
                    new_centers.append(centers[center_index][:])
                else:
                    new_center = [0.0] * dim

                    for point_index in cluster:
                        point = points[point_index]
                        for d in range(dim):
                            new_center[d] += point[d]

                    for d in range(dim):
                        new_center[d] /= len(cluster)

                    new_centers.append(new_center)
            # 步骤 3：判断质心是否基本不再移动
            max_move = 0.0
            for center_index in range(k):
                move = 0.0
                for d in range(dim):
                    diff = new_centers[center_index][d] - centers[center_index][d]
                    move += diff * diff
                # 这里的 move 是移动距离平方，和 eps * eps 比较
                if move > max_move:
                    max_move = move

            centers = new_centers
            final_clusters = clusters

            if max_move < eps * eps:
                break

        counts = []
        for cluster in final_clusters:
            counts.append(len(cluster))

        counts.sort()
        return counts

    answer = solve()
    print(" ".join(map(str, answer)))

if __name__ == '__main__':
    main()
