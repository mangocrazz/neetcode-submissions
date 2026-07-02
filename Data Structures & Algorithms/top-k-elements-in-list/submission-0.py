class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        for i in nums:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        sort_dict = list(sorted(a.items(),key = lambda x:x[1],reverse = True))
        m = []
        for i in range(k):
            m.append(sort_dict[i][0])
        return m