class Stack:
        def __init__(self):
                self.stack = []
                self.top = -1
                
        def Push(self,s):
                self.stack.append(s)
                self.top += 1
                
        def Pop(self):
                if self.Empty():
                        raise Exception("Underflow")
                self.stack.pop()
                self.top -= 1

        # return the index of the top element 
        def Top(self):
                return len(self.stack) - 1

        def Empty(self):
                if self.top < 0:
                        return True
                return False
        
        def toString(self):
                return self.stack

# Q1 Max Stack
class MaxStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
    
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.stack.append(x)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        result = self.stack[-1]
        self.stack.pop()
        return result

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.stack[len(self.stack) - 1]

    """
    @return: An integer
    """
    def peekMax(self):
        # write your code here
        return max(self.stack)

    """
    @return: An integer
    """
    def popMax(self):
        # write your code here
        l = []
        result = 0
        for i in range(len(self.stack)):
            if self.stack[i] == self.peekMax():
                l.append(i)
        result = self.stack[l[-1]]
        self.stack.pop(l[-1])
        return result
            
#Q2 Gas Station
class Solution2(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0 or len(cost) == 0 or sum(gas) < sum(cost):
            return -1
        position = 0
        balance = 0 # current tank balance
        for i in range(len(gas)):
            balance += gas[i] - cost[i] # update balance
            if balance < 0: # balance drops to negative, reset the start position
                balance = 0
                position = i+1
        return position

# Q3 Validate Stack Sequences
class Solution3(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)

# Q4 Dinner Plate Stacks
### my attempt
class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.stacks = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.stacks) == 0:
            self.stacks.append([val])
        else:
            count = 0
            len_rmost = self.stacks[-1]
            while count < len(self.stacks):
                if len(self.stacks[count]) < self.capacity:
                    self.stacks[count].append(val)
                    break
                if len_rmost == self.stacks[-1] and count == len(self.stacks)-1:
                    self.stacks.append([val])
                    break
                count += 1
        #print("Push")
        #print(self.stacks)
                

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stacks) < 1:
            return -1
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        result = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        #print("Pop")
        #print(self.stacks)
        return result
        

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if len(self.stacks) == 0 or index > (len(self.stacks) - 1) or len(self.stacks[index]) == 0:
            return -1 
        result = self.stacks[index].pop(-1)
        #if len(self.stacks[index]) == 0:
            #self.stacks.pop(index)
        #print("popstack:")
        #print(self.stacks)
        return result
### Q4 solution
class DinnerPlatesSolution:
    def __init__(self, capacity):
        self.c = capacity
        self.q = [] # record the available stack, will use heap to quickly find the smallest available stack
        # if you are Java or C++ users, tree map is another good option.
        self.stacks = [] # record values of all stack of plates, its last nonempty stack are the rightmost position

    def push(self, val):
        # To push, we need to find the leftmost available position
        # first, let's remove any stacks on the left that are full
        # 1) self.q: if there is still available stack to insert plate
        # 2) self.q[0] < len(self.stacks): the leftmost available index self.q[0] is smaller than the current size of the stacks
        # 3) len(self.stacks[self.q[0]]) == self.c: the stack has reached full capacity
        while self.q and self.q[0] < len(self.stacks) and len(self.stacks[self.q[0]]) == self.c:
            # we remove the filled stack from the queue of available stacks
            heapq.heappop(self.q)

        # now we reach the leftmost available stack to insert

        # if the q is empty, meaning there are no more available stacks
        if not self.q:
            # open up a new stack to insert
            heapq.heappush(self.q, len(self.stacks))

        # for the newly added stack, add a new stack to self.stacks accordingly
        if self.q[0] == len(self.stacks):
            self.stacks.append([])

        # append the value to the leftmost available stack
        self.stacks[self.q[0]].append(val)

    def pop(self):
        # To pop, we need to find the rightmost nonempty stack
        # 1) stacks is not empty (self.stacks) and
        # 2) the last stack is empty
        while self.stacks and not self.stacks[-1]:
            # we throw away the last empty stack, because we can't pop from it
            self.stacks.pop()

        # now we reach the rightmost nonempty stack

        # we pop the plate from the last nonempty stack of self.stacks by using popAtStack function
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index):
        # To pop from an stack of given index, we need to make sure that it is not empty
        # 1) the index for inserting is valid and，
        # 2) the stack of interest is not empty
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            # we add the index into the available stack
            heapq.heappush(self.q, index)
            # take the top plate, pop it and return its value
            return self.stacks[index].pop()

        # otherwise, return -1 because we can't pop any plate
        return -1

# Q5 Solution
class Solution5(object):
    def __init__(self):
        self.dic = {1:1, 2:2}
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]
if __name__ == '__main__':
    S = Stack()
    print(S.toString())


    print(S.Empty())
    #S.Pop()
    
    S.Push(1)
    S.Push(2)
    S.Push(3)
    print(S.toString())

    S.Pop()
    print(S.toString())
    print(S.Empty())
