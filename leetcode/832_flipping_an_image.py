#Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
#To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
#To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
#
# Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#
# Note!!
# 1 <= A.length = A[0].length <= 20
# 0 <= A[i][j] <= 1
from typing import List


class Solution:
    def flipAndInvertImage(self, arr: List[List[int]]) -> List[List[int]]:
        result = []
        if 1 <= len(arr) == len(arr[0]) <= 20:
            # flip
            for row in arr: # [1, 1, 0]
                # todo: row에 2이상의 값이 있으면 break
                flip = [0 if i == 1 else 0 for i in row]
                result.append(flip)
            # invert
            for row in result:
                row.reverse()
        return result

    def solution2(self, arr: List[List[int]]) -> List[List[int]]:
        for row in arr:
            row.reverse()
        return [[1 - value for value in row] for row in arr]


def test(arr, expected):
    sol = Solution()
    print(len(arr))
    print(len(arr[0]))
    result = sol.solution2(arr)
    assert result == expected, "failed"


if __name__ == '__main__':
    A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    B = [[1, 1, 0, 0], [1, 0, 0, 1],
         [0, 1, 1, 1], [1, 0, 1, 0]]
    result_A = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
    result_B = [[1, 1, 0, 0], [0, 1, 1, 0],
                [0, 0, 0, 1], [1, 0, 1, 0]]
    test(A, result_A)
