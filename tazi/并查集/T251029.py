import sys

def main():
    def solve(lines):
        parent = {}

        for line in lines:
            for elem in line:
                if elem not in parent:
                    parent[elem] = elem
        
        def find(x):
            root = x
            
            while parent[root] != root:
                root = parent[root]

            while x!= root:
                temp = parent[x]
                parent[x] = root
                x = temp

            return root
        
        def union(x,y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                parent[root_x] = root_y
        
        for line in lines:
            if not line:
                continue
            first_elem = line[0]
            for i in range(1,len(line)):
                union(first_elem, line[i])
        
        groups = {}

        for elem in parent:
            root = find(elem)
            if root not in groups:
                groups[root] =[]
            groups[root].append(elem)

        result = list(groups.values())

        for group in result:
            group.sort()

        result.sort()

        return result
    
    n = int(input())

    all_lines = []
    for _ in range(n):
        all_lines.append(input().strip().split())


    result = solve(all_lines)

    for group in result:
        print(' '.join(group)
              )

if __name__ == '__main__':
    main()
