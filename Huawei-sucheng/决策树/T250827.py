import sys

def main():
    # 使用 sys.stdin.readline 读取第一行确定数据量
    # 这样可以适应本地直接粘贴完整输入后按回车运行
    first_line = sys.stdin.readline()
    if not first_line:
        return
    
    # 解析第一行参数
    N, M, K = map(int, first_line.strip().split())
    
    # 为了好对应节点编号，数组大小设为 N+1，第0个元素不用
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    feature = [0] * (N + 1)
    threshold = [0] * (N + 1)
    label = [0] * (N + 1)
    
    # 读取 N 个节点信息
    for i in range(1, N + 1):
        node_info = list(map(int, sys.stdin.readline().strip().split()))
        # 节点行输入顺序为：l_i r_i f_i th_i label_i
        left[i] = node_info[0]
        right[i] = node_info[1]
        feature[i] = node_info[2]
        threshold[i] = node_info[3]
        label[i] = node_info[4]
        
    # 读取 M 行验证集数据
    validation_data = []
    for _ in range(M):
        data_line = list(map(int, sys.stdin.readline().strip().split()))
        validation_data.append(data_line)
        
    # ---------------------------------------------------------
    # 定义核心计算函数 solve
    def solve(N, M, K, left, right, feature, threshold, label, validation_data):
        """
        计算剪枝能获得的最优 F1 分数
        """
        best_f1 = 0.0
        
        # 遍历每一个节点作为剪枝候补节点
        for cand_node in range(1, N + 1):
            
            tp = 0
            fp = 0
            fn = 0
            
            # 遍历验证集的所有样本
            for sample in validation_data:
                # 提取该样本的真实标签（最后一位）
                true_label = sample[-1]
                
                # 模拟当前 sample 在决策树上的预测路径
                cur_node = 1
                while True:
                    # 1. 如果到达了剪枝候选节点，该节点直接变成叶子节点，预测为其 label
                    if cur_node == cand_node:
                        pred_label = label[cur_node]
                        break
                    
                    # 2. 如果当前是原始叶子节点（无左右子节点），预测为其 label
                    if left[cur_node] == 0 and right[cur_node] == 0:
                        pred_label = label[cur_node]
                        break
                    
                    # 3. 否则是内部节点，根据特征和阈值选择路径
                    # 注意：验证集 sample 中特征索引从 0 开始，题目中从 1 开始，所以要 -1
                    f_idx = feature[cur_node] - 1
                    if sample[f_idx] <= threshold[cur_node]:
                        cur_node = left[cur_node]   # 向左子树走
                    else:
                        cur_node = right[cur_node]  # 向右子树走
                
                # 更新 TP, FP, FN
                # 正类情况 (Label = 1)
                if true_label == 1:
                    if pred_label == 1:
                        tp += 1
                    else:
                        fn += 1
                # 负类情况 (Label = 0)
                else:
                    if pred_label == 1:
                        fp += 1
                
            # 计算 Precision 和 Recall
            if tp + fp > 0:
                precision = tp / (tp + fp)
            else:
                precision = 0.0
            
            if tp + fn > 0:
                recall = tp / (tp + fn)
            else:
                recall = 0.0
            
            # 计算 F1
            if precision + recall > 0:
                f1 = 2 * precision * recall / (precision + recall)
            else:
                f1 = 0.0
            
            # 更新全局最优 F1
            if f1 > best_f1:
                best_f1 = f1
                
        return best_f1
    
    # 调用 solve 函数，并拿到结果
    result = solve(N, M, K, left, right, feature, threshold, label, validation_data)
    
    # 输出结果，保留 6 位小数
    print("{:.6f}".format(result))

if __name__ == '__main__':
    main()