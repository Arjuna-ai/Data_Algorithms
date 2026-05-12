import numpy as np

def main():
    n, d, c = map(int,input().split())
    x_data = []
    for _ in range(n):
        x_data.append(list(map(float,input().split())))
    
    w_data = []
    for _ in range(d):
        w_data.append(list(map(float,input().split())))
    
    ratio = float(input())

    X = np.array(x_data,dtype = float)
    W = np.array(w_data, dtype =float)

    def solve(X,W,ratio,n,d,c):
        row_norms = np.sum(np.abs(W),axis=1)

        k = int(ratio * d)
        if ratio > 0:
            if k == 0:
                k = 1
        
        sorted_indices = sorted(range(d), key = lambda i: (row_norms[i], i))
        removed = set(sorted_indices[:k])# 被剪枝层

        keep_indices = []

        # 未剪枝特征下标
        for i in range(d):
            if i not in removed:
                keep_indices.append(i)
        
        # 同步剪枝X的列和W的行
        X_pruned = X[:,keep_indices]
        W_pruned = W[keep_indices,:]

        # 线性变换
        h = X_pruned @ W_pruned

        # softmax
        max_values = np.max(h,axis = 1,keepdims=True)

        exp_values = np.exp(h - max_values)

        sums = np.sum(exp_values,axis =1, keepdims= True)

        # 概率
        y = exp_values / sums

        labels = np.argmax(y,axis=1)# 每一行最大概率对应的下表为标签

        return labels.tolist()
    
    ans = solve(X,W,ratio,n,d,c)
    print(' '.join(map(str,ans)))

if __name__ == '__main__':
    main()
