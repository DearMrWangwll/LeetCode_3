class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        用一个长度与s相同的数组存储，对应位置i存储的是以i为起点的最长子串的长度
        我的思路需要在极端情况下可能需要两次遍历整个字符串时间复杂度为O(n^2)，而如果按照下面的方法通过字典就只可以控制时间复杂度为O(n)
        sum = []
        res = 1
        length = len(s)
        for i in range(length-1):
            j = i+1
            while(s[j] not in s[i:j]):
                res=res+1
                j=j+1
            sum.append(res)
            res = 1
        sum.append(res)
        sum.sort()
        return sum[length-1]
        '''
        # 每读取到一个字母就更新它在字典中的值，改为对应的索引值加一，同时得到以该位置的元素为末尾的最长子串的长度
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans
