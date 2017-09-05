class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = False
        
        if len(s) == 1:
            return ans
        else:
            first = s[0]
            lis = [each for each in xrange(1, len(s)) if s[each] == first]
            if lis == []:
                return ans
            for idx in range(len(lis)):
                check_str = s[0:lis[idx]]
                check_len = len(check_str)
                if len(s) % check_len == 0:
                    if check_str * (len(s)/ check_len) == s:
                        ans = True
        return ans

# -- Best solution --
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = (s+s)[1:-1]
        return ss.find(s) != -1