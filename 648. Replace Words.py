648. Replace Words

In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

# 有点无聊
class Solution:
    def replaceWords(self, dict_: List[str], sentence: str) -> str:
        
        words = sentence.split()
        for pre in dict_:
            for i,w in enumerate(words):
                if w.startswith(pre):
                    words[i]=pre

                    
        return ' '.join(words)
        
        
