722. Remove Comments


Example 1:
Input: 
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]

The line by line code is visualized as below:
/*Test program */
int main()
{ 
  // variable declaration 
int a, b, c;
/* This is a test
   multiline  
   comment for 
   testing */
a = b + c;
}

Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

The line by line code is visualized as below:
int main()
{ 
  
int a, b, c;
a = b + c;
}

Explanation: 
The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4 as comments.


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        source='\n'.join(source)
        
        cur=0
        while('//' in source or '/*' in source):
            bs=source.find('/*',cur)
            cs=source.find('//',cur)
            
            if bs==-1 or (cs!=-1 and cs<bs):# 表示//先出现，或者/*没了，要按顺序删除不然cur对不上
                end=source.find('\n',cs)
                source=source[:cs]+(source[end:] if end!=-1 else '')# 还可以这样写
                cur=cs# 应该这样，说明source已经变了
            else:
                source = source[:bs] + source[source.index('*/', bs+2) + 2:]
                cur = bs

                
        return [x for x in source.split('\n') if x]# 防止空字符
                
