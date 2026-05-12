import sys
import math
from decimal import Decimal, ROUND_HALF_EVEN

def main():
    """
    该部分处理输入
    """
    first_line = sys.stdin.readline().strip()
    if not first_line:
        return

    n, k = map(int, first_line.split())
    points = []

    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x, y))

    def solve(n, k, points):
        """
        根据题意和输入数据，完成核心计算逻辑
        返回需要输出的结果
        """

        def squared_distance_to_center(point, center):
            dx = point[0] - center[0]
            dy = point[1] - center[1]
            return dx * dx + dy * dy

        def format_average(total, count):
            value = Decimal(total) / Decimal(count)
            value = value.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)
            return str(value)

        # 使用前 k 个点作为初始聚类中心
        centers = []
        for i in range(k):
            centers.append([float(points[i][0]), float(points[i][1])])

        labels = [0] * n
        clusters = [[] for _ in range(k)]

        # K-Means 主过程
        for _ in range(100):
            clusters = [[] for _ in range(k)]

            # 1. 将每个点分配给最近的聚类中心
            for i in range(n):
                best_cluster = 0
                best_distance = squared_distance_to_center(points[i], centers[0])

                for c in range(1, k):
                    current_distance = squared_distance_to_center(points[i], centers[c])
                    if current_distance < best_distance:
                        best_distance = current_distance
                        best_cluster = c

                labels[i] = best_cluster # 样本i的簇
                clusters[best_cluster].append(i) # 簇c存样本索引index，互相索引

            # 2. 根据每个簇中的点重新计算中心
            new_centers = []
            for c in range(k):
                if len(clusters[c]) == 0:
                    new_centers.append([centers[c][0], centers[c][1]])
                else:
                    sum_x = 0
                    sum_y = 0
                    for index in clusters[c]:
                        sum_x += points[index][0]
                        sum_y += points[index][1]

                    count = len(clusters[c])
                    new_centers.append([sum_x / count, sum_y / count])

            # 3. 判断是否收敛
            stable = True
            for c in range(k):
                dx = new_centers[c][0] - centers[c][0]
                dy = new_centers[c][1] - centers[c][1]
                move_distance_square = dx * dx + dy * dy

                if move_distance_square > 1e-12:
                    stable = False

            centers = new_centers

            if stable:
                break

        # 预处理任意两个点之间的欧氏距离
        dist_matrix = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                distance = math.hypot(dx, dy)
                dist_matrix[i][j] = distance
                dist_matrix[j][i] = distance

        point_scores = [0.0] * n

        # 计算每个点的轮廓系数
        for i in range(n):
            own_cluster = labels[i]
            own_points = clusters[own_cluster]

            if len(own_points) <= 1:
                point_scores[i] = 1.0
                continue

            # a(i)：到同簇其他点的平均距离
            same_sum = 0.0
            for index in own_points:
                if index != i:
                    same_sum += dist_matrix[i][index]

            a_value = same_sum / (len(own_points) - 1)

            # b(i)：到其他簇平均距离中的最小值
            b_value = None
            for c in range(k):
                if c == own_cluster:
                    continue
                if len(clusters[c]) == 0:
                    continue

                other_sum = 0.0
                for index in clusters[c]:
                    other_sum += dist_matrix[i][index]

                average_distance = other_sum / len(clusters[c])

                if b_value is None:
                    b_value = average_distance
                else:
                    if average_distance < b_value:
                        b_value = average_distance

            if b_value is None:
                point_scores[i] = 1.0
            else:
                denominator = max(a_value, b_value)
                if denominator == 0:
                    point_scores[i] = 0.0
                else:
                    point_scores[i] = (b_value - a_value) / denominator

        # 计算每个簇的平均轮廓系数
        cluster_scores = [1.0] * k
        for c in range(k):
            if len(clusters[c]) == 0:
                cluster_scores[c] = 1.0
            else:
                total_score = 0.0
                for index in clusters[c]:
                    total_score += point_scores[index]

                cluster_scores[c] = total_score / len(clusters[c])

        # 找出轮廓系数最低的簇；若相同，保留编号较小的簇
        worst_cluster = 0
        for c in range(1, k):
            if cluster_scores[c] < cluster_scores[worst_cluster]:
                worst_cluster = c

        # 输出该簇最终中心点坐标，使用 HALF_EVEN 保留两位小数
        if len(clusters[worst_cluster]) == 0:
            x_text = str(Decimal(str(centers[worst_cluster][0])).quantize(
                Decimal("0.01"),
                rounding=ROUND_HALF_EVEN
            ))
            y_text = str(Decimal(str(centers[worst_cluster][1])).quantize(
                Decimal("0.01"),
                rounding=ROUND_HALF_EVEN
            ))
        else:
            sum_x = 0
            sum_y = 0
            for index in clusters[worst_cluster]:
                sum_x += points[index][0]
                sum_y += points[index][1]

            count = len(clusters[worst_cluster])
            x_text = format_average(sum_x, count)
            y_text = format_average(sum_y, count)

        return x_text + "," + y_text

    result = solve(n, k, points)
    print(result)

if __name__ == '__main__':
    main()
