import sys
import numpy as np

def main():
    def solve(input_data):
        n = len(input_data)
        if n == 0:
            return 0
        
        vetors = []
        dim = -1
        for item in input_data:
            if len(item) < 2:
                return 0
            v = [float(x) for x in item[1:]]
            vetors.append(v)
            if dim == -1:
                dim = len(v)
            elif len(v) != dim:
                return 0
            
        if n == 1:
            return 1
        
        mat = np.array(vetors)
        norms = np.sqrt(np.sum(mat * mat,axis = 1, keepdims = True))
        norms[norms < 1e-8] =1.0

        norms_mat = mat/(norms)

        sims = norms_mat @ norms_mat.T

        parents = list(range(n))

        size = [1] * n

        def find(x):
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return 
            if size[root_x] < size[root_y]:
                root_x,root_y = root_y, root_x
            parents[root_y] = root_x
            size[root_x] += size[root_y]

        for i in range(n):
            for j in range(i + 1, n):
                if sims[i][j] >= 0.95:
                    union(i,j)
        max_size = max(size)
        return max_size if max_size > 1 else 1
    
    input_data = sys.stdin.read().strip().splitlines()

    data = []
    for line in input_data:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        data.append(parts)
    result = solve(data)
    print(result)

if __name__ == '__main__':
    main()
