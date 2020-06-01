import math

class Solution(object):
	def constructRectangle(area):
		lis = []
		for i in range(1, area + 1):
			if area % i == 0:
				lis.append((int(i), int(area/i)))
		target = round(len(lis)/2)
		answer = sorted(lis[target])
		print([answer[-1], answer[0]])
		# if len(lis) % 2 == 0:
			# print(lis[len(lis % 2) + 1])

        """
        :type area: int
        :rtype: List[int]
        """
        test = math.sqrt(area)
        test_b = math.ceil(test)
        test_a = math.floor(test)
        print(test_a)
        print(test_b)

        Solution.check(test_a, test_b, area)

    def check(ans_a, ans_b, area):
        if area == ans_a*ans_b:
        	print(ans_b, ans_a)
        elif area == ans_a*area:
        	print(ans_a, area)
        else:
            ans_a = ans_a-1
            ans_b = area
            Solution.check(ans_a, ans_b, area)

Solution.constructRectangle(8)