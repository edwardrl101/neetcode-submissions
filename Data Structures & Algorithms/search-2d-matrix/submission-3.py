class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix)-1
        while u <= d:
            m = (u+d)//2
            if matrix[m][0] > target:
                d = m - 1
            else:
                l, r = 0, len(matrix[0])-1
                while l <= r:
                    mm = (l+r)//2
                    if matrix[m][mm] == target:
                        return True
                    if matrix[m][mm] < target:
                        l = mm + 1
                    else:
                        r = mm - 1
                u = m + 1
        return False