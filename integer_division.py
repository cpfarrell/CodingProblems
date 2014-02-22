class Solution:
    # @return an integer
    def flip(self, integer):
        integer -= (integer + integer)
        return integer

    def divide(self, dividend, divisor):
        if divisor == 0:
            return float("infinity")

        

        neg = False
        if (divisor < 0 and dividend > 0) or (divisor>0 and dividend<0):
            neg = True

        if divisor < 0:
            divisor = self.flip(divisor)

        if dividend < 0:
            dividend = self.flip(dividend)

        total = divisor
        count = 0
        while total <= dividend:
            count += 1
            total += divisor
        if neg:
            count = self.flip(count)
        return count

s = Solution()
print s.divide(1,-1)
