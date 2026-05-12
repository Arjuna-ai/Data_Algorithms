from collections import deque
def main():
    tokens = input().strip().split()
    u,k = map(int,input().split())

    def solve(tokens, u, k):
        class Node:
            def __init__(self,val):
                self.val = val
                self.left = None
                self.right = None
                self.parent = None
        
        def build_tree():
            # 构建二叉树，记录目标节点
            if len(tokens) == 0:
                return None, None
            if tokens[0] == '#':
                return None, None
            
            root = Node(int(tokens[0]))
            target = None

            if root.val == u:
                target = root
                
            queue = deque()
            queue.append(root)
            index = 1

            while len(queue) > 0:
                node  = queue.popleft()

                if index >= len(tokens):
                    break

                token = tokens[index]
                index += 1

                if token != '#':
                    child = Node(int(token))
                    child.parent = node
                    node.left = child
                    queue.append(child)

                    if target is None:
                        if child.val == u:
                            target = child
                
                if index >= len(tokens):
                    break

                token = tokens[index]
                index += 1

                if token != '#':
                    child = Node(int(token))
                    child.parent = node
                    node.right = child
                    queue.append(child)

                    if target is None:
                        if child.val == u:
                            target = child

            return root, target
        
        if k <= 0:
            return -1

        root, target = build_tree()

        if root is None:
            return -1
        if target is None:
            return -1

        # 收集目标节点的祖先
        ancester_set = set()
        node = target.parent

        while node is not None:
            ancester_set.add(node)
            node = node.parent
        
        # 中序遍历
        before_values = []
        stack = []
        node = root

        while True:
            while node is not None:
                stack.append(node)
                node = node.left
            if len(stack) == 0:
                break

            node = stack.pop()

            if node is target:
                break

            if node in ancester_set:
                before_values.append(node.val)

            node = node.right

        if len(before_values) < k:
            return -1
        
        return before_values[k-1]
    
    result = solve(tokens, u, k)
    print(result)

if __name__=='__main__':
    main()