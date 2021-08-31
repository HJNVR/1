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
            
# Q1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        def dfs(root):
            if not root:
                return
            if low <= root.val <= high:
                self.res += root.val
            if low <= root.val:
                dfs(root.left)
            if high >= root.val:
                dfs(root.right)
        self.res = 0
        dfs(root)
        return self.res
        
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
