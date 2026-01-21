class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x):
            return int(str(x)[::-1])
        
        # Key: number, Value: latest index where reverse(nums[i]) equals this number
        reverse_map = {}
        min_dist = float('inf')
        
        for j, num in enumerate(nums):
            # Check if current number equals reverse of some earlier number
            if num in reverse_map:
                min_dist = min(min_dist, j - reverse_map[num])
            # Store/update reverse of current number with current index
            # We want the latest index to minimize distance with future numbers
            rev = reverse(num)
            reverse_map[rev] = j  # Always update to latest index
        
        return min_dist if min_dist != float('inf') else -1