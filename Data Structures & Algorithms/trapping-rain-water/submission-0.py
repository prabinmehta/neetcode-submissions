class Solution:
    def trap(self, height: List[int]) -> int:
        #[0,2,2,3,3,3,3,3,3,3]
        #[3,3,3,3,3,3,3,3,2,1]
        prefix_max = [0]*len(height)
        suffix_max = [0]*len(height)
        max_prefix=height[0]
        max_suffix=height[-1]
        for i,j in enumerate(height):
            # print(i,j)
            if j>=max_prefix:
                max_prefix = j
            prefix_max[i]=max_prefix
            # print(prefix_max)
        for i in range(len(height)-1,-1,-1):
            # print(i, height[i])
            if height[i]>=max_suffix:
                max_suffix= height[i]
                # print(max_suffix)
            suffix_max[i]=max_suffix
            # print(suffix_max)
        # print(suffix_max,prefix_max)
        res = 0
        for i in range(len(suffix_max)):
            res+=min(suffix_max[i],prefix_max[i])-height[i]
        return res


