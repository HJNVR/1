# Q1 Solution
class Solution1(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen, res = [0] * len(nums), 0
        for i in nums:
            cnt = 0
            while not seen[i]:
                seen[i], cnt, i = 1, cnt + 1, nums[i]
            res = max(res, cnt)
        return res

# Q2 Solution
class Solution2(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(i,j):
            if j-i < 0:
                return [None]
            elif j-i == 0:
                return [TreeNode(i)]
            else:
                res = []
                for k in range(i,j+1):
                    left = generate(i,k-1)
                    right = generate(k+1,j)
                    for l in left:
                        for r in right:
                            root = TreeNode(k)
                            root.left = l
                            root.right = r
                            res.append(root)
                return res
        if n == 0:
            return []
        else:
            return generate(1,n)
