class Solution(object):
    def reverse(self, x):
        temp=abs(x)
        rev=0
        while temp>0:
            digit=temp%10
            rev=rev*10+digit
            temp=temp//10
        if x<0:
            rev=-rev
        if (-2**31<=rev<=2**31):
            return rev
        else:
            return 0

        