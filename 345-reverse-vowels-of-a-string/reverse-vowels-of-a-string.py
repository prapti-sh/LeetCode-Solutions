class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        p1 = 0
        p2 = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s1 = list(s)

        while p1 < p2:
            if s1[p1] in vowels and s1[p2] in vowels:
                s1[p1] , s1[p2] = s1[p2], s1[p1]
                p1 += 1
                p2 -= 1
            elif s1[p1] in vowels :
                p2 -= 1
            elif s1[p2] in vowels:
                p1 +=1
            else:
                p1 += 1
                p2 -= 1
        return "".join(s1)



        
        