class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums = sorted(nums)

        i = 0
        while (i < len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while (left < right):
                if nums[left] + nums[right] + nums[i] > 0:
                    right -= 1

                    while (right > 0 and nums[right] == nums[right+1]):
                        right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1

                    while (left < len(nums) and nums[left] == nums[left-1]):
                        left += 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    right -= 1

                    while (right > 0 and nums[right] == nums[right+1]):
                        right -= 1

                    left += 1 
                    while (left < len(nums) and nums[left] == nums[left-1]):
                        left += 1
            
            i += 1
            while (i < len(nums) - 1 and nums[i] == nums[i-1]):
                i += 1

        return triplets