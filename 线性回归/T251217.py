import numpy as np

def main():
    k = int(input())
    train_nums = []
    while len(train_nums) < 4 * k:
        nums = list(map(int,input().split()))
        train_nums.extend(nums)

    train = np.array(train_nums,dtype = float).reshape(k,4)

    n = int(input())
    test_num = []
    while len(test_num) < 3 *n:
        nums = list(map(int,input().split()))
        test_num.extend(nums)

    test = np.array(test_num,dtype= float).reshape(n,3)

    def gauss_solve(a, b):
        size = len(b)
        aug = np.concatenate((a.copy(),b.reshape(size,1)),axis=1)
        for col in range(size):
            pivot = col
            for row in range(col + 1, size):
                if abs(aug[row][col]) > abs(aug[pivot][col]):
                    pivot = row
            if pivot != col:
                tmp = aug[col].copy()
                aug[col] = aug[pivot]
                aug[pivot] = tmp

            div = aug[col][col]
            aug[col] = aug[col]/ div

            for row in range(size):
                if row != col:
                    factor = aug[row][col]
                    if abs(factor) > 1e-12:
                        aug[row] = aug[row] - factor * aug[col]

        return aug[:,size]
    
    def solve(train_data,test_data):
        ones = np.ones((train_data.shape[0], 1))
        x = np.concatenate((ones,train_data[:,:3]),axis=1)
        y = train_data[:,3]

        # 正规方程
        a = x.T @ x
        b = x.T @ y

        coef  = gauss_solve(a,b)

        test_ones = np.ones((test_data.shape[0],1))
        test_x = np.concatenate((test_ones,test_data),axis=1)
        preds = test_x @ coef

        ans = []

        for value in preds:
            ans.append(int(value+0.5))
        return ans
    result = solve(train,test)
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()

