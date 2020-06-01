class Solution(object):
    def findComplement(num):
        """
        :type num: int
        :rtype: int
        """
        if num / 2 != 0:
            list.append(num % 2)
            num = int(num/2)
            Solution.findComplement(num)
        elif num == 1:
            list.append(num)
        # print(list)
list = []
Solution.findComplement(6)
print(list)

for i in range(len(list), -1, -1):
    print(list[i])