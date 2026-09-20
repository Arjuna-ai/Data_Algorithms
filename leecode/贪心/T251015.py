import numpy as np
import sys

def main():
    input = sys.stdin.readline
    first_line = input().strip()
    n,d = map(int,first_line.split())

    # token
    X_list = []
    for _ in range(n):
        row = list(map(float,input().strip().split()))
        X_list.append(row)

    # c_j
    c_list = list(map(int,input().strip().split()))


    def solve(n,d,X_list,c_list):
        X = np.array(X_list)
        c = np.array(c_list)

        rms = np.sqrt(np.mean(X ** 2, axis = 1,keepdims= True))

        X_hat= X / rms
        scores = np.dot(X_hat,X_hat.T) / np.sqrt(d)

        scores_squared = scores ** 2

        total_scores = 0.0

        for j in range(1,n):
            vec = scores_squared[:j,j]

            k = c[j]

            if k == 0:
                continue
            if len(vec) > k:
                sorted_vec = np.sort(vec)[::-1]
                top_k_sum = np.sum(sorted_vec[:k])
            else:
                top_k_sum = np.sum(vec)

            total_scores += top_k_sum
        
        return int(round(100 * total_scores))


    result = solve(n,d,X_list,c_list)

    print(result)

if __name__ == '__main__':
    main()
        

