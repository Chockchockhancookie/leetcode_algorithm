class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            tmp = nums[i] + dp[i-1]
            if tmp > nums[i]:
                dp[i] = tmp
            else:
                dp[i] = nums[i]
        
        return max(dp)