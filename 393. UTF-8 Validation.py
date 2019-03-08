393. UTF-8 Validation

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.



class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        def check(rest,i):
            if len(rest)!=i:
                return False
            for i in rest:
                if not i.startswith('10'):
                    return False
            return True
                
        data=[bin(x)[2:].zfill(8) for x in data]# bin,zfill有用
        
        index=0
        while(index<len(data)):
            if data[index].startswith('0'):
                index+=1
            elif data[index].startswith('110'):
                if index+1>=len(data):
                    return False
                else:
                    if not check(data[index+1:index+2],1):
                        return False
                    index+=2
            elif data[index].startswith('1110'):
                if index+2>=len(data):
                    return False
                else:
                    if not check(data[index+1:index+3],2):
                        return False
                    index+=3
            elif data[index].startswith('11110'):
                if index+3>=len(data):
                    return False
                else:
                    if not check(data[index+1:index+4],3):
                        return False
                    index+=4
            else:
                return False# 就是说其它方式不允许
            
        
        return True
         
        
