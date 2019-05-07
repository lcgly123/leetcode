900. RLE Iterator

Write an iterator that iterates through a run-length encoded sequence.

The iterator is initialized by RLEIterator(int[] A), where A is a run-length encoding of some sequence. 
More specifically, for all even i, A[i] tells us the number of times that the non-negative integer value A[i+1] 
is repeated in the sequence.

The iterator supports one function: next(int n), which exhausts the next n elements (n >= 1)
and returns the last element exhausted in this way.  If there is no element left to exhaust, next returns -1 instead.

For example, we start with A = [3,8,0,9,2,5], which is a run-length encoding of the sequence [8,8,8,5,5]. 
This is because the sequence can be read as "three eights, zero nines, two fives".

class RLEIterator:

    
    
    
    # 题意：给定一个数组，偶数位表示下一个位置的数字出现的次数，奇数位表示数字；
    # 例如给定数组A=[3,8,0,9,2,5]表示的结果序列应当是有3个8、0个9、和2个5，
    # 即sequence=[8,8,8,5,5]；现要求模拟迭代器，构建next函数，实现遍历sequence；
    def __init__(self, A: List[int]):
        self.s=A
        self.i=0#对应偶数位
        
    # 其实不难
    def next(self, n: int) -> int:
        if self.i>=len(self.s):
            return -1
        if self.s[self.i]>n:
            self.s[self.i]-=n
            return self.s[self.i+1]
        elif self.s[self.i]==n:
            self.i+=2
            return self.s[self.i-2+1]
        else:
            self.i+=2
            return self.next(n-self.s[self.i-2])# NB
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)




