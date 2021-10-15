class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        k = len(flowerbed)
        for i in range(k-2):
            if i==0:
                if flowerbed[i]==flowerbed[i+1]==0:
                    flowerbed[0]=1
                    n-=1
            else:
                if flowerbed[i]==flowerbed[i+1]==flowerbed[i+2]==0:
                    flowerbed[i+1]=1
                    n-=1
        if flowerbed[k-2]==flowerbed[k-1]==0:
            flowerbed[k-1]=1
            n-=1
        if n<=0:
            return True
        return False