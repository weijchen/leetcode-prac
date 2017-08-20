class Solution(object):
    def twoSum(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            ans_a = numbers[i]
            divide = numbers[i+1:]
            for j in range(len(divide)):
                ans_b = divide[j]
                if target <= 0:
                    return [i+1, i+j+2]
                if ans_b < target:
                    if ans_a + ans_b == target:
                        return [i+1, i+j+2]
                        break

numbers = [0,0, 3, 4]
target = 0
ans = Solution.twoSum(numbers, target)
print(ans)