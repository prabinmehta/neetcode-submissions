class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchb(nums,target,l,r):
            if l>r:
                return -1
            mid = (l+r+1)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                return searchb(nums,target,mid+1,r)
            else:
                return searchb(nums,target,l,mid-1)
        return searchb(nums,target,0,len(nums)-1)
        