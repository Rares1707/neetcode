class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        total_size = n * m
        start, end = 0, total_size - 1

        while start <= end:
            mid = (start + end) // 2
            i = mid // m
            j = mid - i * m

            element = matrix[i][j]
            if element == target:
                return True
            elif element < target:
                start = mid + 1
            else:
                end = mid - 1

        return False
