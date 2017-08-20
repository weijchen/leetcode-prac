class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        lis_a = (a, b)
        lis_b = (1, 1)
        return sum(p*q for p,q in zip(lis_a, lis_b))