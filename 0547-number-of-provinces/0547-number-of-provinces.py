class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
    # create a dynmaically change dict that maps an index to the set to which it rightly belongs. Note that the set if marked by the latest elements in the set in the process of iteration. we merge the relevant sets if we found the current index linked previous sets
        indexToSet = defaultdict()
        
        for i, neighbors in enumerate(M):
            newSet = set() 
            newSet.add(i) # i must be an element in the new set
            setKeysDelete = set()
            for j, jsneighbors in indexToSet.items():
                for k in jsneighbors:
                    if neighbors[k] == 1:
                        newSet.update(jsneighbors)
                        setKeysDelete.add(j)
                        break #no need to update new set with set j and delete key j multiple times
            for j in setKeysDelete:
                indexToSet.pop(j, None)
            indexToSet[i] = newSet
        return len(indexToSet.keys())