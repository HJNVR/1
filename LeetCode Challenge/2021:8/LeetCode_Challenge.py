# Q1
class Solution(object):
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

