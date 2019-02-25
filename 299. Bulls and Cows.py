299. Bulls and Cows

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 题有问题
        secret=list(map(int,secret))
        guess=list(map(int,guess))
        
        bull=0
        l1=[0]*10# 真值中有几个这个数字（1-9）
        l2=[0]*10# 猜到这个数字但位置不对的有几个
        # 上面俩中的最小值就是cow，这就是定义吧
        for i in range(len(guess)):
            if secret[i]==guess[i] :
                bull+=1
            else:
                l1[secret[i]]+=1
                l2[guess[i]]+=1
                
        cow=sum(map(min,zip(l1,l2)))# 这说明sum可以直接对迭代器求和
                    
        return '{}A{}B'.format(bull,cow)
