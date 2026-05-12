import sys
def main():
    def solve(s):
        last_idx = [-1] * 128

        left = 0
        max_len = 0

        for r , ch in enumerate(s):
            code = ord(ch)
            if last_idx[code] >= left:# 出现过
                left = last_idx[code] + 1
            last_idx[code] = r

            cur_len = r - left + 1
            if cur_len > max_len:
                max_len  = cur_len
        
        return max_len
    
    s = sys.stdin.readline().strip()

    result = solve(s)

    print(result)

if __name__ == '__main__':
    main()
            