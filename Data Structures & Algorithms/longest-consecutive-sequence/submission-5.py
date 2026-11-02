class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set=set()
        arr=[[] for i in range(len(nums)+1)]
        i=0
        count=1
        while i<len(nums):
            prev=nums[i]-1
            plus=nums[i]+1
            while prev in my_set:
                count+=1
                prev-=1
            while plus in my_set:
                count+=1
                plus+=1
            print("Index: " + str(i) + " Count: " + str(count))
            arr[count].append(count)
            my_set.add(nums[i])
            i+=1
            count=1
        if(len(nums)==0):
            return 0

        for i in range(len(arr)-1, 0, -1):
            for num in arr[i]:
                return num
        
    