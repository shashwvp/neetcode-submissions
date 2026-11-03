class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] = d[nums[i]] + 1
            else:
                d[nums[i]] = 1
        sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        for key in sorted_d:
            if len(l) == k:
                break
            l.append(key)
        return l

