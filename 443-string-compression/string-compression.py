class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        size = 0
        s = ""
        lastCh = chars[0]

        for ch in chars:
            if ch != lastCh:
                s = s + lastCh
                if size > 1:
                    s = s + str(size)
                size = 1
                lastCh = ch
            else:
                size += 1

        s = s + lastCh
        if size > 1:
            s = s + str(size)

        i = 0
        for c in s:
            chars[i] = c
            i += 1
        
        return len(s)

            



            



        