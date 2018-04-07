# Single Number
#
# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?



class Solution:
    #解法一  异或运算符
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for i in A:
        # 相同元素异或为0,0与任何数异或等于任何数，有a^b^a = b
        # 此外，异或还可以用于两个元素交换a=a^b^(b=a)
            result = result^i
        return(result)


class Solution:
    # 解法二
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1

        for k, v in d.items():
            if v == 1:
                return k