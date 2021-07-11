class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # answer = s[::-1]    # 릿코드에서만 오류!
        answer = s.reverse()
        return answer