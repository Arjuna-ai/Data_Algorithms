import sys
import numpy as np

def main():
    k, m, n, s = map(int,input().split())

    test_sample_row = list(map(float,input().split()))
    test_sample = np.array(test_sample_row)

    X_raw = []
    y_raw = []
    for _ in range(m):
        data_line = list(map(float,input().split()))
        X_raw.append(data_line[:n])
        y_raw.append(int(data_line[-1]))

    X = np.array(X_raw)
    y = np.array(y_raw)

    def solve(k, test_arr, X_arr, y_arr):
        diff  = X_arr - test_arr
        squared_diff = diff ** 2
        sum_diff = np.sum(squared_diff,axis = 1)
        distances = np.sqrt(sum_diff)

        # 排序，取前k个索引
        sort_indices = np.argsort(distances)
        k_indices = sort_indices[:k]
        
        # 获取前k个的距离
        k_distances = distances[k_indices]

        # 获取这k个的标签
        k_labels = y_arr[k_indices]

        # 统计频次
        unique_labels, labels_counts = np.unique(k_labels,return_counts=True)

        # 找频次最大标签
        max_count = np.max(labels_counts)

        max_label_indices = np.where(labels_counts == max_count)[0]
        max_labels = unique_labels[max_label_indices]

        if len(max_labels) == 1:
            best_label = max_labels[0]
        else:
            best_label = max_labels[0]
            min_dist = float('inf')
            for i in range(k):
                curr_label = k_labels[i]
                if curr_label in max_labels:
                    curr_dist = k_distances[i]
                    if curr_dist < min_dist:
                        min_dist = curr_dist
                        best_label = curr_label
        
        return best_label,max_count
    
    result_label,result_count = solve(k,test_sample,X,y)

    print(f'{result_label} {result_count}')

if __name__ == '__main__':
    main()



