# Q1
class Solution1(object):
    def findLUSlength(self, strs):
        def check(s1,s2):
            A = len(s1)
            B =len(s2)
            while (A > 0 and B > 0):
                i = len(s1) - A 
                j = len(s2) - B
                if(s1[i] == s2[j]):
                    A -= 1 
                B -= 1
            return A == 0
        
        maxLen = -1 
        n=len(strs)
        for i in range(n):
            flag = 0
            currLen = len(strs[i])
            for j in range(n):
                if(i != j and check(strs[i],strs[j]) == 1):
                    flag = 1 
                    break 
            if(flag == 0):
                maxLen = max(maxLen , currLen)
        return maxLen

# Q2
class Solution2(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        ans, nsum = 0, 0
        nums.append(n+1)
        for i in nums:
            num = min(i,n+1)
            while nsum + 1 < num:
                print(nsum)
                nsum += nsum + 1
                ans += 1
            nsum += num # add all the sum
        return ans

# Q3
class Solution3(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m*n
        return min(op[0] for op in ops)*min(op[1] for op in ops)
