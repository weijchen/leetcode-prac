def findGoodStrings(n, s1, s2, evil):
    """
    :type n: int
    :type s1: str
    :type s2: str
    :type evil: str
    :rtype: int
    """
    # check prefix
    evil_len = len(evil)
    if s1[:evil_len] == evil and s2[:evil_len] == evil:
    	print(0)
    	# return 0
    else:
    	s1_sum = sum([ord(char) for char in s1])
    	s2_sum = sum([ord(char) for char in s2])
    	print(s1_sum, s2_sum)

# 2
# "aa"
# "da"
# "b"
# 8
# "leetcode"
# "leetgoes"
# "leet"
# 2
# "gx"
# "gz"
# "x"
# findGoodStrings(2, "aa", "da", "b")
findGoodStrings(8, "leetcode", "leetgoes", "leet")


