468. Validate IP Address

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.



class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        # ipv4：有4段，每段数字不以0（除非就是0），-开头，<=0,>=255
        # ipv6：有8段，每段1到4位，所有字符都在 '0123456789abcdefABCDEF'内
        def check_ipv4(ip):
            for i in ip:
                if i.isdigit()==False or str(int(i))!=i or int(i)<0 or int(i)>255:# str(int(i))==i表示不以0开头，不是负数,有用
                    return False
            return True
        def check_ipv6(ip):
            for part in ip:
                if len(part)>4 or len(part)<1:# 有用
                    return False
                else:
                    for c in part:
                        if c not in '0123456789abcdefABCDEF':
                            return False
                
            return True
            
        if len(IP.split('.'))==4:
            ip=IP.split('.')
            return 'IPv4' if check_ipv4(ip) else 'Neither'
        elif len(IP.split(':'))==8:
            ip=IP.split(':')
            print(ip)
            return 'IPv6' if check_ipv6(ip) else 'Neither'
        else:
            return 'Neither'
        
        
        
