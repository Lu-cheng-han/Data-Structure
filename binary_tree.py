class BinaryTreeNode:

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    @staticmethod
    def print_tree(node:'BinaryTreeNode', level = 0, prefix="Root: "):
        if node is not None:
            print("  " * level + prefix + str(node.data))
            node.print_tree(node.left, level + 1, "L--- ")
            node.print_tree(node.right, level + 1, "R--- ")

    @staticmethod
    def insert_node(root: 'BinaryTreeNode', data):
        if root is None:
            return BinaryTreeNode(data)
        
        if data < root.data:
            root.left = BinaryTreeNode.insert_node(root.left,data)

        if data > root.data:
            root.right = BinaryTreeNode.insert_node(root.right,data)
        
        return root

if __name__ == "__main__":
    # 创建二叉树
    # root = BinaryTreeNode(1)
    # root.left = BinaryTreeNode(2)
    # root.right = BinaryTreeNode(3)
    # root.left.left = BinaryTreeNode(4)
    # root.left.right = BinaryTreeNode(5)
    # root.right.left = BinaryTreeNode(6)
    # root.right.right = BinaryTreeNode(7)

    root = None
    node_data = [1, 6, 9 , 19 ,44 ,96 ,3, 11]
    for data in node_data:
        root = BinaryTreeNode.insert_node(root, data)
        
    # 打印二叉树
    BinaryTreeNode.print_tree(root)