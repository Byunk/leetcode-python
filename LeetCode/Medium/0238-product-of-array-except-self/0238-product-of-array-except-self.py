class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        p = 1
        for i in range(len(nums)):
            result.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= p
            p *= nums[i]

        return result