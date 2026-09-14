class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            print(i)
            if s[i] == "(":
                print("Stack add")
                stack.append(i)
            else:
                stack.pop()
                print("Stack pop")
                if len(stack) == 0:
                    print("Stack add in 0")
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len



        