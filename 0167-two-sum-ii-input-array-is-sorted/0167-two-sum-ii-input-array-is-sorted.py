class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {};
        for i in range(len(numbers)):
            if target - numbers[i] in dict:
                return [dict[target - numbers[i]] + 1, i + 1]
            else: 
                dict[numbers[i]] = i