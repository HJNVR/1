def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

# Q1: Find the Minimum Number of Fibonacci Numbers Whose Sums is K

## My Attempt : Success but slow
class MySolution(object):
    '''
    Input: k = 7
    Output: 2 
    Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
    For k = 7 we can use 2 + 5 = 7.
    >>> s = Solution()
    >>> s.findMinFibonacciNumbers(7)
    '''
    def fib(self,n):
        if 0<=n<=1:
            return n
        return self.fib(n-1) + self.fib(n-2)
    
    def findmax(self,l,k):
        # l is now reversed from large to small
        for i in l:
            if i <= k:
                return i
        
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        l = []
        count = 0
        while self.fib(count) <= k:
            l.append(self.fib(count))
            count +=1
        
        l.reverse()
        
        fib_sum = 0
        result = 0
        k_copy = k
        while fib_sum <= k:
            fib_sum += self.findmax(l,k_copy)
            k_copy = k_copy - self.findmax(l,k_copy)
            result += 1
            if fib_sum == k:
                break
        return result

## Solution
class Solution(object):
        
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k<=1:
            return k
        a,b = 1,1
        while b <= k:
            a,b = b,a+b
        return self.findMinFibonacciNumbers(k-a) + 1

    #Q2 solution
    def lenLongestFibSubseq(self, A):
        s = set(A)
        res = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a, b, l = A[i], A[j], 2
                while a + b in s:
                    a, b, l = b, a + b, l + 1
                res = max(res, l)
        return res if res > 2 else 0


