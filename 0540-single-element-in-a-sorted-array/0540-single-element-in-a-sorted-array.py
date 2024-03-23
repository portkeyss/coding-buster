class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (end - start)//2 + start
            if mid - 1 >= 0 and nums[mid] == nums[mid-1]:
                if (mid + 1 - start) % 2 == 1:
                    end = mid - 2
                else:
                    start = mid + 1
            elif mid + 1 < len(nums) and nums[mid] == nums[mid+1]:
                if (mid + 1- start) % 2 == 1:
                    start = mid + 2
                else:
                    end = mid - 1
            else:
                return nums[mid]