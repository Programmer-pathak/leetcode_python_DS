class Solution:
    def addDigits(self, num):
        while num>=10:
            num=self.operation(num)
        return num

    def operation(self,num):
        l=[]
        while num!=0:
            digit=num%10
            l.append(digit)
            num=num//10
        return sum(l)
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.addDigits(38))
    ttt