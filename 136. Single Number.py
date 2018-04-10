# 给定一个整数数组，除了某个元素外其余元素均出现两次。请找出这个只出现一次的元素。
#
#
#
# 备注：
#
# 你的算法应该是一个线性时间复杂度。 你可以不用额外空间来实现它吗？

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1

        for num, counter in d.items():
            if counter == 1:
                return num