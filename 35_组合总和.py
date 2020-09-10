#!/user/bin/env python
# -*- coding:utf-8 -*-
'''
@author: JJon_Boat
@e-mail: 1125922211@qq.com
@time: 2020/9/9 6:59 下午
@product: PyCharm
@desc:

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例 2：
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 
提示：
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500
'''

class Solution:
    def combinationSum(self, candidates: list, target: int):
        def recursion(left_list, target, current_list):
            for i in range(len(left_list)):
                if left_list[i] > target:
                    return None
                elif left_list[i] == target:
                    result.append(current_list + [left_list[i]])
                else:
                    if left_list[i] <= target-left_list[i]:
                        recursion(left_list[i:], target-left_list[i], current_list+[left_list[i]])

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
    candidates = [2, 3, 5]
    target = 8
    print(Solution.combinationSum(candidates,target))

    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution.combinationSum(candidates, target))