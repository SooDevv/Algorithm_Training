class Solution:
    def sortArrayByParity(self, arr: List[int]) -> List[int]:
        even = [i for i in arr if i % 2 == 0]
        odd = [i for i in arr if i % 2 != 0]
        return even + odd