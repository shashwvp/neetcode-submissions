class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        maxCount = 0
        for i in range(len(nums)):
            nextNumInSeq = nums[i]+1
            count = 1
            if nums[i]-1 not in hs: # filter out when not start of sequence
                while nextNumInSeq in hs:
                    count += 1
                    nextNumInSeq += 1
                if count > maxCount:
                    maxCount = count
                    print("Sequence starts at: ", nums[i], "count: ", maxCount)
        return maxCount