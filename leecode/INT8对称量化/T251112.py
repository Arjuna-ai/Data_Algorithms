import sys
import numpy as np

def main():
    input_line = sys.stdin.readline
    n = int(input_line().strip())
    x = np.array(list(map(float,input_line().strip().split())),dtype = float)

    m , col = map(int,input_line().strip().split())

    rows = []

    for _ in range(m):
        row = list(map(float,input_line().strip().split()))
        rows.append(row)
    W = np.array(rows, dtype=float)

    def round_half_up(value):
        return int(value + 0.5 + 1e-9)
    
    def quantize(v):
        # INT8量化
        v_min = float(np.min(v))
        v_max = float(np.max(v))
        scale = (v_max- v_min) / 255.0

        if scale == 0:
            q = np.full(v.shape, -128, dtype=np.int64)
        else:
            q = np.rint((v-v_min) / scale) -128
            q = np.clip(q,-128,127).astype(np.int64)
        
        return q, scale, v_min
    
    def dequantize(q,scale,v_min):
        # 将量化整数反量化为浮点数
        return (q.astype(float) + 128.0) * scale + v_min
    
    def solve(x, W):
        x_quant,x_scale,x_min = quantize(x)
        W_quant,W_scale,W_min = quantize(W)

        # 使用量化整数计算全连接输出
        y_int = W_quant @ x_quant

        # 反量化
        x_dequant = dequantize(x_quant,x_scale,x_min)
        W_dequant = dequantize(W_quant,W_scale,W_min)

        y_float  = W @ x
        y_dequant = W_dequant @ x_dequant

        diff = y_float - y_dequant

        mse = float(np.mean(diff * diff))

        mse_result = round_half_up(mse * 100000.0)

        first_line = ' '.join(str(int(num)) for num in y_int)
        return [first_line, str(mse_result)] 
    
    result = solve(x,W)
    print('\n'.join(result))

if __name__ == '__main__':
    main()


    

