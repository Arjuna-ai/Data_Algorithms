import numpy as np

def main():
    line = input().split(',')
    L = int(line[0])
    D = int(line[1])
    K = int(line[2])
    eta = float(line[3])

    y_true = list(map(float,input().split(',')))

    X_vals = list(map(float, input().split(',')))
    X_data = np.array(X_vals).reshape(L,D)

    W_mlp_vals = list(map(float,input().split(',')))
    W_mlp_data = np.array(W_mlp_vals).reshape(D,D)

    W_cls_vals = list(map(float,input().split(',')))
    W_cls_data = np.array(W_cls_vals).reshape(D,K)

    def solve(L, D, K, eta, y_true, X, W_mlp, W_cls):
        W_cls_old = W_cls.copy()
        h = np.mean(X, axis = 0,keepdims=True)
        h_out = h @ W_mlp
        y_pred = h_out @ W_cls

        # 计算损失
        loss = np.mean((y_pred- y_true) ** 2)

        # 反向传播与更新
        g = (2.0 / K) * (y_pred - y_true)

        # 更新w_cls
        dw_cls = h_out.T @ g
        W_cls = W_cls - eta * dw_cls

        # 更新w_mlp

        delta = g @ W_cls_old.T
        dw_mlp = h.T @ delta
        W_mlp = W_mlp - eta * dw_mlp

        pred_list = [f'{val:.2f}' for val in y_pred.flatten()]
        loss_str = f'{loss:.2f}'
        w_mlp_list = [f'{val:.2f}' for val in W_mlp.flatten()]
        w_cls_list = [f'{val:.2f}' for val in W_cls.flatten()]

        return pred_list, loss_str, w_mlp_list,w_cls_list
    
    pred_list, loss_str, w_mlp_list,w_cls_list = solve(L,D,K,eta,
            np.array(y_true),
            X_data,
            W_mlp_data,
            W_cls_data)
    
    print(','.join(pred_list))
    print(loss_str)
    print(','.join(w_mlp_list))
    print(','.join(w_cls_list))

if __name__ == '__main__':
    main()


