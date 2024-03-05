class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        mySet = set(nums)
        for i in mySet:
            if i - 1 not in mySet:
                curr, length = i, 0
                while curr in mySet:
                    length += 1
                    curr += 1
                if length > longest:
                    longest = length
        return longest

s =  Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
