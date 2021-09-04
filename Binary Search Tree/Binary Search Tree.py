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

# Q2
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        L = []
        def dfs(node):
            if node.left: dfs(node.left)
            L.append(node.val)
            if node.right: dfs(node.right)
        dfs(root)
        #print(L)
        abs_mins = []
        for i in range(len(L)-1):
            abs_mins.append(abs(L[i]-L[i+1]))
        return min(abs_mins)
            
        #return min(b - a for a, b in zip(L, L[1:]))

# Q3 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution3(object):
    pre = -float('inf')
    res = float('inf')
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left:
            self.getMinimumDifference(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        #print(self.res)
        #print(self.pre)
        if root.right:
            self.getMinimumDifference(root.right)
        return self.res

# Q4 solve by myself

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution4(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        l = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)
        #print(l)
        for i in range(len(l)-1):
            for j in range(i+1,len(l)):
                if (l[i]+l[j]) == k:
                    return True
        return False

# Q5
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution5(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: # if root doesn't exist, just return it
		    return root
        if root.val > key:# if key value is less than root value, find the node in the left subtree
            root.left = self.deleteNode(root.left, key)
        elif root.val < key: # if key value is greater than root value, find the node in right subtree
		    root.right= self.deleteNode(root.right, key)
        else: #if we found the node (root.value == key), start to delete it
		    if not root.right: # if it doesn't have right children, we delete the node then new root would be root.left
                #print(root.val)
			    return root.left
		    if not root.left: # if it has no left children, we delete the node then new root would be root.right
			    return root.right
		    temp = root.right
            #print(temp.val)
            #print(root.val)
		    mini = temp.val
		    while temp.left:
			    temp = temp.left
			    mini = temp.val
		    root.val = mini # replace value
		    root.right = self.deleteNode(root.right,root.val) # delete the minimum node in right subtree
        return root
        
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
