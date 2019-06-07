380. Insert Delete GetRandom O(1)

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = {}
        self.arr = []
        self.length = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.s:
            return False
        else:
            self.arr.append(val)
            self.length += 1
            self.s[val] = self.length-1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.s:
            idx = self.s[val]
            last = self.arr[self.length-1]
            self.arr[idx] = last
            self.s[last] = idx
            del self.s[val]
            self.arr.pop()
            self.length -= 1
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0,self.length-1)
        return self.arr[idx]
