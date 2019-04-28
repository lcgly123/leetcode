735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        
        for m in asteroids:
            if m>0:
                stack.append(m)
            else:
                # 处理流程NB,好像学不来啊,试了几次，也只能这样了
                # 必须先把小的正的弹出来，再看看有没有相当的，最后再把负的装进去
                while(stack and stack[-1]>0 and stack[-1]<abs(m)):
                    stack.pop()
                if stack==[] or stack[-1]<0:
                    stack.append(m)    
                elif stack[-1]==-m:
                    stack.pop()

                    
        
        return stack
                
                        
        







