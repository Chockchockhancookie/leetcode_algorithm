class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = list(itertools.permutations(nums))
        return answer