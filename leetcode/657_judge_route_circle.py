class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        v = 0
        h = 0
        for char in moves:
            if char == 'U':
                # print('hi')
                h += 1
            elif char == 'D':
                h -= 1
            elif char == 'L':
                v -= 1
            elif char == 'R':
                v += 1
        if v == 0 and h == 0:
            return True
        else:
            return False