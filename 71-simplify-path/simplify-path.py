class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathEle = path.split("/")
        ans = ""
        stack = []

        for ele in pathEle:
            if ele == "..":
                if stack: 
                    stack.pop()
            elif ele == "." or ele == "":
                continue
            else:
                stack.append(ele)

        if stack: 
            while stack:
                ele = stack.pop()
                ans = "/" + ele + ans
        else:
            return "/"

        return ans
            


        