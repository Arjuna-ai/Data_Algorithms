import sys
import math

def main():
    line = sys.stdin.readline().strip()

    parts = line.split()

    eps = float(parts[0])
    min_samples = int(parts[1])
    x = int(parts[2])

    points = []
    for _ in range(x):
        line_data = list(map(float, input().split()))
        points.append(line_data)
    def solve(eps, min_samples, points):
        n = len(points)
        if n == 0:
            return 0, 0
        # 距离函数
        dim = len(points[0])

        def distance(p1,p2):
            s = 0.0
            for i in range(dim):
                diff = p1[i] - p2[i]
                s += diff * diff
            return math.sqrt(s)
        
        # 获取eps领域
        def get_neighbors(idx):
            neighbors = []
            p = points[idx]
            for i in range(n):
                if i == idx:
                    continue
                if distance(p,points[i]) <= eps:
                    neighbors.append(i)
            return neighbors
        
        labels = [0]* n
        visited = [False] * n
        cluster_id = 0

        # 扩展一个簇
    
        def expand_cluster(start_idx, neighbors, cid):
            labels[start_idx] = cid
            i = 0
            while i < len(neighbors):
                curr_idx = neighbors[i]
                if not visited[curr_idx]:
                    visited[curr_idx] =True
                    curr_neighbors = get_neighbors(curr_idx)
                    if len(curr_neighbors) >= min_samples:
                        for nb in curr_neighbors:
                            if nb not in neighbors:
                                neighbors.append(nb)
                if labels[curr_idx] <= 0:
                    labels[curr_idx] = cid
                i += 1

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                neighbors = get_neighbors(i)
                if len(neighbors) < min_samples:
                    labels[i] = -1 # 噪声
                else:
                    cluster_id += 1
                    expand_cluster(i, neighbors, cluster_id)
        
        num_clusters = cluster_id
        num_noise = labels.count(-1)
        return num_clusters, num_noise
    
    result = solve(eps, min_samples, points)

    print(result[0], result[1])

if __name__ == '__main__':
    main()


            


        