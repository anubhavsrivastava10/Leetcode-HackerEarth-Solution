class Solution:
    def minPartitions(self, n: str) -> int:
        val = 0
        for item in n:
            if int(item)>val:
                val = int(item)
        return val