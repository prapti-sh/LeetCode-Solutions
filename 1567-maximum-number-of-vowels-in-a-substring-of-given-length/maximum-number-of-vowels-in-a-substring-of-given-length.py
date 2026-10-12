class Solution(object):
    def isVowel(self, ch):
        if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
            return True
        return False

    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowelCount = 0
        for ch in s[:k]:
            if self.isVowel(ch):
                vowelCount += 1
        if vowelCount == k or k>len(s):
            return k
        maxVowel = vowelCount
        

        for i in range(k,len(s)):
            if self.isVowel(s[i]):
                vowelCount += 1
            
            if self.isVowel(s[i-k]):
                vowelCount += -1
            maxVowel = max(vowelCount, maxVowel)

            if maxVowel == k:
                return k

        return maxVowel
            


        