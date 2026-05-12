from collections import deque
import sys

sys.setrecursionlimit(1000000)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(tokens):
    """根据层序序列构建二叉树，# 表示空节点"""
    if len(tokens) == 0:
        return None

    if tokens[0] == "#":
        return None

    root = TreeNode(int(tokens[0]))
    queue = deque()
    queue.append(root)

    index = 1

    while queue:
        node = queue.popleft()

        if index >= len(tokens):
            break

        # 处理左孩子
        if tokens[index] != "#":
            left_node = TreeNode(int(tokens[index]))
            node.left = left_node
            queue.append(left_node)

        index += 1

        if index >= len(tokens):
            break

        # 处理右孩子
        if tokens[index] != "#":
            right_node = TreeNode(int(tokens[index]))
            node.right = right_node
            queue.append(right_node)

        index += 1

    return root


def inorder_traverse(node, inorder_list, parent):
    """中序遍历，同时记录父节点关系"""
    if node is None:
        return

    if node.left is not None:
        parent[node.left.val] = node.val

    if node.right is not None:
        parent[node.right.val] = node.val

    inorder_traverse(node.left, inorder_list, parent)
    inorder_list.append(node.val)
    inorder_traverse(node.right, inorder_list, parent)


def solve():
    level_tokens = input().strip().split()
    u, k = map(int, input().strip().split())

    root = build_tree(level_tokens)

    if root is None:
        print(-1)
        return

    inorder_list = []
    parent = {}

    inorder_traverse(root, inorder_list, parent)

    # 判断节点 u 是否存在
    pos = {}
    for i in range(len(inorder_list)):
        pos[inorder_list[i]] = i

    if u not in pos:
        print(-1)
        return

    # 找到 u 的所有祖先
    ancestor_set = set()
    cur = u

    while True:
        if cur in parent:
            father = parent[cur]
            ancestor_set.add(father)
            cur = father
        else:
            break

    count = 0

    # 只扫描中序序列中位于 u 前面的节点
    for val in inorder_list:
        if val == u:
            break

        if val in ancestor_set:
            count += 1

            if count == k:
                print(val)
                return

    print(-1)


if __name__ == "__main__":
    solve()
