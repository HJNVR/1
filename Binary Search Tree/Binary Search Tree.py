class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.value)
        self.inorder(root.right)

    def poster(self, root):
        if not root:
            return
        self.poster(root.left)
        self.poster(root.right)
        print(root.value)

    def preorder(self, root):
        if not root:
            return
        print(root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def search(self,root,k):
        if not root or root.value == k:
            return root
        if k < root.value:
            return self.search(root.left,k)
        else:
            return self.search(root.right,k)

    def Max(self, root):
        if not root.right:
            return root
        return self.Max(root.right)

    def Min(self, root):
        if not root.left:
            return root
        return self.Min(root.left)
            

if __name__ == '__main__':
    BST = Node(6)
    BST.left = Node(4)
    BST.right = Node(7)
    BST.left.left = Node(2)
    BST.left.right = Node(5)
    BST.right.right = Node(8)

    # inorder
    print("inorder")
    BST.inorder(BST)

    # poster
    print("poster")
    BST.poster(BST)

    # preorder
    print("preorder")
    BST.preorder(BST)
