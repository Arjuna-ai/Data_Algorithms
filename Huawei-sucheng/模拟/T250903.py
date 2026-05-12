
def main():
    n, m, p, k = map(int,input().split())

    probs = list(map(float,input().split()))

    def solve(n,m,p,k,probs):
        if n % m != 0:
            return 'error'
        
        group_size = n // m

        # 2. 判断选定的 p 个组中专家数量是否足够选出 k 个
        if p * group_size < k:
            return 'error'
        
        group_max = [] # 存放元组(最大概率，组索引)

        for i in range(m):
            start_index = i * group_size
            end_index = start_index + group_size
            max_prob = max(probs[start_index:end_index])
            group_max.append((max_prob, i))

        # 按照概率降序排列,取前p个
        group_max.sort(key = lambda x:x[0],reverse= True) # 按照概率降序排列

        selected_groups = []
        for j in range(p):
            selected_groups.append(group_max[j][1])

        #4. 将选定的 p 个组里的所有专家概率和编号加入候选列表
        candidates = []

        for g_index in selected_groups:
            start_index = g_index * group_size
            end_index = start_index + group_size

            for idx in range(start_index,end_index):
                candidates.append((probs[idx], idx))
            
        if len(candidates) < k:
            return 'error'
        candidates.sort(key = lambda x:x[0],reverse= True)
        final_ids = []
        for t in range(k):
            final_ids.append(candidates[t][1])

        # 最终专家编号按升序排列并返回
        final_ids.sort()
        return ' '.join(map(str, final_ids))
    
    result = solve(n,m,p,k,probs)
    print(result)

if __name__ == '__main__':
    main()

