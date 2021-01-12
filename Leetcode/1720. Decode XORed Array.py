class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        lst = [first]
        for item in encoded:
            first = first^item
            lst.append(first)
        return lst