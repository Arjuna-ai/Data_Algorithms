import sys

def main():
    def solve(pred,trueY, weights):
        N = len(weights)

        conf = [[0]* N for _ in range(N)]
        m = len(pred)
        for i in range(m):
            p = pred[i]
            t = trueY[i]
            if 0 <= p < N and 0 <= t < N:
                conf[t][p] += 1
        
        total_precision = 0.0
        total_recall = 0.0
        total_f1 = 0.0

        for i in range(N):
            # 真正例 (TP)：真实为 i 且预测为 i
            Tp= conf[i][i]
            # 计算假正例 (FP)：预测列 i 之和减去 TP
            col_sum = 0
            for j in range(N):
                col_sum += conf[j][i]
            Fp = col_sum - Tp

            # 计算假负例 (FN)：真实行 i 之和减去 TP
            row_sum = 0
            for k in range(N):
                row_sum += conf[i][k]
            Fn = row_sum - Tp

            # 计算当前的 Precision（处理分母为零的情况）
            if Tp + Fp == 0:
                curr_precision = 0.0
            else:
                curr_precision = Tp /(Tp + Fp)

            # 计算当前的 Recall（处理分母为零的情况）
            if Tp + Fn == 0:
                curr_recall =0.0
            else:
                curr_recall = Tp/(Tp + Fn)
            
            if curr_precision + curr_recall == 0.0:
                curr_f1 = 0.0
            else:
                curr_f1 = 2 * curr_precision * curr_recall /(curr_recall + curr_precision)
            
            total_precision += weights[i] * curr_precision
            total_recall += weights[i] * curr_recall
            total_f1 += weights[i] * curr_f1
        return total_precision,total_recall,total_f1
    
    pred_line = list(map(int,input().split()))
    trueY_line = list(map(int,input().split()))
    weights = list(map(float,input().split()))

    precision, recall, f1 = solve(pred_line,trueY_line,weights)

    print(f'{precision:.2f} {recall:.2f} {f1:.2f}')

if __name__ == '__main__':
    main()

    
