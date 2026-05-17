class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchMatrixRow(matrix,target,lm,rm):
            if lm>rm:
                return -1
            mid = (lm+rm+1)//2
            first = matrix[mid][0]
            last = matrix[mid][-1]
            if target>=first and target<=last:
                return mid
            elif target>=first and target>last:
                return searchMatrixRow(matrix,target,mid+1,rm)
            else:
                return searchMatrixRow(matrix,target,lm,mid-1)
        
        def searchMatricCol(matrix, target, ln, rn):
            if ln>rn:
                return False
            mid = (ln+rn+1)//2
            if target==matrix[mid]:
                return True
            elif target>matrix[mid]:
                return searchMatricCol(matrix,target,mid+1,rn)
            else:
                return searchMatricCol(matrix,target,ln,mid-1)
        rm = len(matrix)-1
        m = searchMatrixRow(matrix,target,0,rm)
        print(m)
        if m == -1:
            return False
        rn = len(matrix[0])-1
        return searchMatricCol(matrix[m],target,0,rn)

            
        