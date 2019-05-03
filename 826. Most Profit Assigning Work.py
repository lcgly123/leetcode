826. Most Profit Assigning Work

We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job. 

Now we have some workers. worker[i] is the ability of the ith worker, which means that this worker can only complete a job with difficulty at most worker[i]. 

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.  If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100 
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        # 多个人可以拿同一个工作，其实不难
        job=list(zip(profit,difficulty))# 按利润，然后按难度
        job.sort(reverse=True)
        
        worker.sort(reverse=True)
        
        i=0
        j=0
        res=0
        while(i<len(worker) and j<len(job)):
            if worker[i]>=job[j][1]:
                res+=job[j][0]
                i+=1
            else:
                j+=1
                
        return res
                
        
