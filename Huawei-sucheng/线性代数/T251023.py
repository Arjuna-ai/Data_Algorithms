import sys
import numpy as np

def main():
    a, m, o = map(int,input().split())

    image_data = [] # A = [[0,1,...],[0,1,...],...],约定 A[y][x]
    for _ in range(a):
        row = list(map(int,sys.stdin.readline().split()))
        image_data.append(row)

    M = [] # [a,b,tx],[c,d,ty]
    for _ in range(m):
        row = list(map(int,sys.stdin.readline().split()))
        M.append(row)
    
    size_data = []
    for _ in range(o):
        row = list(map(int,sys.stdin.readline().split()))
        size_data.extend(row)

    h = size_data[0]
    w = size_data[1]

    def solve(image_data,M,h,w):
        image = np.array(image_data,dtype=int)
        Mat = np.array(M,dtype=int)
        result = np.zeros((h,w),dtype=int)

        src_h,src_w = image.shape
        a,b,tx = Mat[0]
        c,d,ty = Mat[1]

        for y in range(src_h):
            for x in range(src_w):
                new_x = a * x + b * y + tx
                new_y = c * x + d * y + ty

                inside = True

                if new_y < 0 or new_y >= h:
                    inside = False
                if new_x < 0 or new_x >= w:
                    inside = False
                if inside:
                    result[new_y][new_x] = image[y][x]
        return result.reshape(-1).tolist()
    
    answer = solve(image_data, M, h, w)
    print(' '.join(map(str,answer)))

if __name__ == '__main__':
    main()

    