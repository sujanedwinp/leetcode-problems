
# https://leetcode.com/problems/add-binary/

class Solution(object):
    def addBinary(self, a:str, b:str):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a=="0" and b=="0":
            return "0"
        # print(f"a: {a}")
        # print(f"b: {b}")

        
        diff=abs(len(a)-len(b))
        if len(a)<len(b):
            a=("0"*diff)+a
        elif len(b)<len(a):
            b=("0"*diff)+b
        
        a=a[::-1]
        b=b[::-1]
        sum=[]
        carry=0
        # print(f"REV a: {a}")
        # print(f"REV b: {b}")
        for i in range(0, len(a)):
            aBit=a[i]
            bBit=b[i]
            # 3
            if aBit=="1" and bBit=="1" and carry==1:
                sum.append("1")
                carry=1
            # 2
            elif ((aBit=="1" or bBit=="1") and carry==1) or (aBit=="1" and bBit=="1"):
                sum.append("0")
                carry=1
            # 1
            elif aBit=="1" or bBit=="1" or carry==1:
                sum.append("1")
                carry=0
            # 0
            else:
                sum.append("0")
        
        if carry==1:
            sum.append("1")
                
        return ''.join(sum[::-1]) 


a="11"
b="1"
print(Solution().addBinary(a,b))