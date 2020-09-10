#!/user/bin/env python
# -*- coding:utf-8 -*-
'''
@author: JJon_Boat
@e-mail: 1125922211@qq.com
@time: 2020/9/10 8:23 下午
@product: PyCharm
@desc:

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
class Solution:
    def twoSum(self, nums, target):

        dic = {}
        # 第一次遍历：num作为key，index作为value，构建字典
        for index,num in enumerate(nums):
            dic[num] = index

        # 从字典，寻找是否有（target-num）作为key的值
        for index,num in enumerate(nums):
            # 字典有get方法，get(key)的key若不存在，则返回为空，可以作为False的判断条件
            if dic.get(target-num) and dic.get(target-num) != index:
                return [index, dic[target-num]]

if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9

    print(s.twoSum(nums,target))