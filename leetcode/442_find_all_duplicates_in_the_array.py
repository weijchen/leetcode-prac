class Solution(object):
    def findDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        anslis = []
        if len(nums) > 1:
            for i in range(1, len(nums)):
                check_a = nums[i-1]
                check_b = nums[i]
                if check_a == check_b:
                    anslis.append(check_a)
            return anslis  
        else:
            return []
r = Solution.findDuplicates([4,3,2,7,8,2,3,1])
print(r)

# # -- Best solution --
# class Solution(object):
#     def findDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         result = []
#         dict = {}
#         for num in nums:
#             if num not in dict:
#                 dict[num] = 1
#             else:
#                 result.append(num)
#         return result