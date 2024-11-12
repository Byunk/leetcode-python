class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[0])

        max_beauty = items[0][1]
        for i in range(len(items)):
            max_beauty = max(max_beauty, items[i][1])
            items[i][1] = max_beauty
        
        return [self.binary_search(items, target) for target in queries]

    def binary_search(self, arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        if r < 0:
            return 0
            
        return arr[r][1]
