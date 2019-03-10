406. Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 想法很NB，个矮的插进去不会影响个高的，只要同等身高的才会彼此影响，所以按要求前面人的个数从小到大插进去，所以这种题给的数据不合适排不了
        mid=sorted(people,key=lambda x:(-x[0],x[1]))
        
        res=[]
        for x in mid:
            res.insert(x[1],x)
            
        return res
            
        
        
        
        
        
