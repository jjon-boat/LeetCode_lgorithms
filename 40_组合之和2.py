#!/user/bin/env python
# -*- coding:utf-8 -*-
'''
@author: JJon_Boat
@e-mail: 1125922211@qq.com
@time: 2020/9/10 7:47 下午
@product: PyCharm
@desc:
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
'''

class Solution:
    def combinationSum2(self, candidates: list, target: int):
        def recursion(left_list, target, current_list):
            for i in range(len(left_list)):
                if i > 0 and left_list[i] == left_list[i-1]:
                    # 重复的元素不作为首个元素重新遍历一遍
                    pass
                else:
                    if left_list[i] > target:
                        return None
                    elif left_list[i] == target:
                        result.append(current_list + [left_list[i]])
                    else:
                        if left_list[i] <= target-left_list[i]:
                            recursion(left_list[i+1:], target-left_list[i], current_list+[left_list[i]])

        candidates.sort()
        n = len(candidates) - 1
        for i in range(len(candidates)):
            if candidates[i] >= target:
                n = i
                break
        candidates = candidates[:n + 1]
        result = []
        recursion(candidates, target, [])
        return result

if __name__ == '__main__':
    Solution = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(Solution.combinationSum(candidates,target))

    candidates = [2,5,2,1,2]
    target = 5
    print(Solution.combinationSum(candidates, target))
