class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        p1 = 0
        p2 = 0

        while p2<len(chars):
            lastCh = chars[p2]
            size = 0
            while p2<len(chars) and  chars[p2] == lastCh:
                p2 += 1
                size += 1
                
            chars[p1] = lastCh
            p1 +=1
            if size > 1:
                for ch in str(size):
                    chars[p1] = ch
                    p1 +=1
                
            
        return p1
        
                

            


                
            

            



            



        