class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        x = set(nums1)
        for item in x:
            if nums1.count(item)==nums2.count(item):
                if nums1.count(item)!=0:
                    z = [item]*nums1.count(item)
                    lst.extend(z)
            elif nums1.count(item)<nums2.count(item):
                if nums1.count(item)!=0:
                    z = [item]*nums1.count(item)
                    lst.extend(z)
            elif nums1.count(item)>nums2.count(item):
                if nums2.count(item)!=0:
                    z = [item]*nums2.count(item)
                    lst.extend(z)
        return lst