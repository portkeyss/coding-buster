class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dictionary = defaultdict(list) #map distinct numbers to list of indices
        for i, num in enumerate(nums):
            self.dictionary[num] += [i]

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.dictionary[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)