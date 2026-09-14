class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {"(":")", "{":"}", "[":"]"}
        stack = []
        for c in s:
            if c in mapping.keys():
                stack.append(c)
            elif stack and mapping.get(stack[-1]) == c:
                stack.pop()
            else :
                return False
        return not stack

        