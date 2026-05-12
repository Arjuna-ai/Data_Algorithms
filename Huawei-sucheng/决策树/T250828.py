class Node:
    def __init__(self, feature_index, threshold, left, right, lable):
        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left
        self.right = right
        self.lable = lable

f, m, n = map(int,input().split())

tree = []
for _ in range(m):
    fi, thr, l, r, lable = input().split()
    tree.append(Node(int(fi), float(thr), int(l),int(r), int(lable)))

for _ in range(n):
    features = list(map(float,input().split()))
    current = 0
    while True:
        node = tree[current]
        if node.feature_index == -1:
            print(node.lable)
            break
        if features[node.feature_index] <= node.threshold:
            current = node.left
        else:
            current = node.right