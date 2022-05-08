# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


#using recurssion is the key and understanding how to use the above given class
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        def flat(nestedList):
            flatlist = []
            for i in nestedList:
                if i.isInteger():
                    flatlist.append(i.getInteger())
                else:
                    flatlist.extend(flat(i.getList()))
            return flatlist
        
        self.lst = flat(nestedList)
    
    def next(self) -> int:
        return self.lst.pop(0)
    
    def hasNext(self) -> bool:
         return len(self.lst)>0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())