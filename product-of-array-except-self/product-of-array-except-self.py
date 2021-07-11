class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        a = 1
        for i in range(len(nums)):
            answer.append(a)
            a *= nums[i]
        a = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= a
            a *= nums[i]
        return answer