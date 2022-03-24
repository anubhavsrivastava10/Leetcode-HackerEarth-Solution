class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start = 0
        end = len(people)-1
        count = 0
        while(start<=end):
            cost = people[start]+people[end]
            if cost>limit:
                end -= 1
                count += 1
            else:
                start += 1
                end -= 1
                count += 1
        return count