#!/user/bin/env python
# -*- coding:utf-8 -*-
'''
@author: JJon_Boat
@e-mail: 1125922211@qq.com
@time: 2020/9/8 7:54 下午
@product: PyCharm
@desc:

给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
示例:
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution:
    def combine(self, n: int, k: int):
    # def combine(self, n: int, k: int):
        def recursion(remain_list:list,remain_num:int,prefix:list):
            '''
            :param remain_list(list): 剩下的数字从这个list中选
            :param remain_num(int): 还差几个数字
            :param prefix(list): 已经有的前缀
            :return: None
            '''
            if remain_num==0:
                result.append(prefix[:])
                # prefix和prefix[:]的区别是prefix[:]为浅拷贝。
                # 如果不加浅拷贝，直接append的话，后面prefix一改变，result中的所有元素也会跟着改变
            tmp_length = len(remain_list)
            for i in range(tmp_length):
                if len(remain_list[i+1:])>=remain_num-1:  # 剪枝，能大大提升运行效率
                    recursion(remain_list[i+1:], remain_num-1, prefix+[remain_list[i]])
                    # prefix+[remain_list[i]] :list+list = list连接
                else: break

        nums = list(range(1,n+1))
        result = []
        recursion(nums,k,[])
        return result


if __name__ == '__main__':
    Solution = Solution()
    print(Solution.combine(4,3))