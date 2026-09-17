class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        l = len(flowerbed)

        for i in range(l):
            if n==0:
                break

            if flowerbed[i] == 0 and i == 0 and l == 1:
                n -= 1
                flowerbed[i] = 1
            elif flowerbed[i] == 0 and i == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
            elif flowerbed[i] == 0 and i == l-1 and flowerbed[i-1] == 0:
                n -= 1
                flowerbed[i] = 1
            elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
        return n == 0
            

        