import ast
import numpy as np

def main():
    # 输入

    n,m,h = map(int,input().split())

    def solve(n, m, h):
        # 1) 构造 X 全 1，W 上三角全 1
        X = np.ones((n,m), dtype = float)
        W = np.triu(np.ones((m,h),dtype = float))

        # 2) 计算 Q, K, V（矩阵乘法）
        Q = X @ W
        K = X @ W
        V = X @ W

        # 3) 计算 M=(Q·K^T)/sqrt(h)
        M = (Q @ K.T) / np.sqrt(float(h))

        # 4) “简化 softmax”：按行除以行和

        row_sum = M.sum(axis = 1, keepdims = True)

        A = M / (row_sum + 1e-12)

        Y = A @ V

        total = float(Y.sum())

        return int(np.rint(total))
    
    result = solve(n, m, h)

    print(result)

if __name__ == "__main__":
    main()

        

