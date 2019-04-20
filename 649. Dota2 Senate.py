649. Dota2 Senate

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        # 题目意思大概是，两拨人，如果第一拨人出现，第二拨人的第一个就要到最后去，直到有一拨人都没了，
        #感觉没啥意思
        mem_num=len(senate)
        
        R=[i for i in range(mem_num) if senate[i]=='R']
        D=[i for i in range(mem_num) if senate[i]=='D']
        
        # 说明while 每次都会计算（记得for不会每次都计算）
        while(len(R) and len(D)):
            if D[0]>R[0]:
                R.append(R[0]+mem_num)
            else:
                D.append(D[0]+mem_num)
            
            D.pop(0)
            R.pop(0)
            
        return "Dire" if len(D) != 0 else "Radiant"
        
        
        
