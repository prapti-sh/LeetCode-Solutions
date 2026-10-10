class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        tp = 0
        sp = 0
        ans = True


        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
            
            
        return sp == len(s)


                    



            
            

        