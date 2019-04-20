641. Design Circular Deque

Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k=k
        self.data=[]
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.data)==self.k:
            return False
        else:
            self.data.insert(0,value)
            return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.data)==self.k:
            return False
        else:
            self.data.append(value)
            return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.data)==0:
            return False
        else:
            self.data.pop(0)
            return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.data)==0:
            return False
        else:
            self.data.pop()
            return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.data[0] if len(self.data)>0 else -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.data[-1] if len(self.data)>0 else -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.data==[]
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.data)==self.k
        


