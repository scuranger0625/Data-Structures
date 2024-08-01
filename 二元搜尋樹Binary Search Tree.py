class TreeNode:
    # 定義二元搜尋樹的節點
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    # 初始化二元搜尋樹
    def __init__(self):
        self.root = None

    def insert(self, key):
        # 插入元素到二元搜尋樹中
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        # 遞迴插入元素到正確的位置
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        # 查找二元搜尋樹中的元素
        return self._search(self.root, key)

    def _search(self, node, key):
        # 遞迴查找元素
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        # 刪除二元搜尋樹中的元素
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        # 遞迴刪除元素並調整樹結構
        if node is None:
            return node

        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            # 找到節點，進行刪除
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # 有兩個子節點，找到後繼節點替代
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)

        return node

    def _min_value_node(self, node):
        # 找到最小值節點（後繼節點）
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        # 中序遍歷二元搜尋樹（輸出所有節點的值）
        return self._inorder(self.root)

    def _inorder(self, node):
        res = []
        if node:
            res = self._inorder(node.left)
            res.append(node.val)
            res = res + self._inorder(node.right)
        return res

# 創建並操作二元搜尋樹的示例
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder traversal:", bst.inorder())  # 輸出 [20, 30, 40, 50, 60, 70, 80]

# 查找節點
result = bst.search(40)
print("Search for 40:", result.val if result else "Not found")  # 輸出 40

# 刪除節點
bst.delete(20)
print("Inorder traversal after deleting 20:", bst.inorder())  # 輸出 [30, 40, 50, 60, 70, 80]

# 重要事項：
# - 二元搜尋樹是一種樹形資料結構，每個節點最多有兩個子節點，
#   左子節點的值小於根節點的值，右子節點的值大於根節點的值。
# - 二元搜尋樹允許高效地進行插入、刪除和查找操作，
#   平均時間複雜度為 O(log n)，最差情況下為 O(n)。
# - 中序遍歷二元搜尋樹可以得到有序的元素序列。
