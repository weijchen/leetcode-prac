class Solution(object):
	def combinationSum4(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		dp = [1] + [0] * target
		for i in xrange(target + 1):
			for x in nums:
				if i + x <= target:
					dp[i + x] += dp[i]
		return dp[target]