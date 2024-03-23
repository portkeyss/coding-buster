"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        self.idxMap = {}
        for i,em in enumerate(employees):
            self.idxMap[em.id] = i
        return self.getImp(employees, id)
    
    def getImp(self, employees, id):
        if employees[self.idxMap[id]].subordinates == []:
            return employees[self.idxMap[id]].importance
        importance = employees[self.idxMap[id]].importance
        for sub in employees[self.idxMap[id]].subordinates:
            importance += self.getImp(employees, sub)
        return importance