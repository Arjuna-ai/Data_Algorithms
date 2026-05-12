import sys

def iou(box1, box2):
    w1, h1 = box1
    w2, h2 = box2
    intersection = min(w1,w2) * min(h1,h2)
    union = w1 * h1 + w2 * h2 - intersection

    return intersection/ (union + 1e-16)

def calc_distance(box1, box2):
    return 1- iou(box1, box2)

def solve(n, k, T, boxes):
    # 取前k个检测框作为迭代起点
    centers = boxes[:k]
    for _ in range(T):
        clusters = []
        for _ in range(k):
            clusters.append([])

        # 分配
        for box in boxes:
            best_index = 0
            best_distance = calc_distance(box,centers[0])

            for i in range(1,k):
                current_distance = calc_distance(box,centers[i])
                if current_distance < best_distance:
                    best_distance = current_distance
                    best_index = i
            clusters[best_index].append(box)

        # 更新：计算每个簇的中心(宽，高)
        new_centers = []
        for i in range(k):
            cluster = clusters[i]

            if len(cluster) == 0:
                new_centers.append(clusters[i]) # 为什么不是直接new_centers.append(cluster)？
            else:
                total_w = 0
                total_h = 0
                for w, h in cluster:
                    total_w +=w
                    total_h +=h
                count = len(cluster)
                new_w = total_w // count
                new_h = total_h // count
                new_centers.append((new_w,new_h))
        
        # 判断迭代收敛条件
        total_shift = 0.0
        for i in range(k):
            total_shift += calc_distance(centers[i],new_centers[i])
        centers = new_centers

        if total_shift < 1e-4:
            break
        
    centers.sort(key = lambda x:x[0] *x[1],reverse= True)

    return centers

def main():
    n,k,T = map(int,input().split())
    boxes = []

    for _ in range(n):
        w,h = map(int,input().split())
        boxes.append((w,h))

    result = solve(n, k, T, boxes)

    output = []
    for w, h in result:
        output.append(str(w)+ ' '+str(h))

    print('\n'.join(output))

if __name__ == '__main__':
    main()

    