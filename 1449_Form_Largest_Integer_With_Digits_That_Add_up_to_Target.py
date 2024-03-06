# Bottom up DP
# class Solution(object):
#     def largestNumber(self, cost, target):
#         """
#         :type cost: List[int]
#         :type target: int
#         :rtype: str
#         """
#         dp = [] # stores the largest num we can reach, for a given target
#         dp.append("0")
#         i = 1
#         while i <= target:
#             curMax = "0"
#             for k in range(0,9):
#                 prev = i-cost[k]
#                 if prev < 0 or (dp[prev] == "0" and prev != 0 ): continue
#                 cur = str(k+1) if dp[prev] == "0" else dp[prev] + str(k+1)
#                 if curMax == "0" or len(curMax) < len(cur) or (len(curMax) == len(cur) and cur > curMax):
#                     curMax = cur
#             dp.append(curMax)
#             i += 1
#         return dp[target]

# Top down DP
class Solution(object):

    def largestNumber(self, cost, target):
        """
        :type cost: List[int]
        :type target: int
        :rtype: str
        """
        dp = dict()
        return self.largestNumberDP(cost, target, dp)


    def largestNumberDP(self, cost, target, dp):
        if target not in dp.keys():
            max = "0"
            for i in range(0,9):
                prevCost = target-cost[i]
                if prevCost < 0: continue
                if prevCost == 0:
                    cur = str(i+1)
                else:
                    prev = self.largestNumberDP(cost, prevCost, dp)
                    if prev == "0": continue
                    cur = prev + str(i+1)
                if len(cur) > len(max) or (len(cur) == len(max) and cur > max):
                    max = cur
            dp[target] = max
        return dp[target]




s = Solution()
# print(s.largestNumber([4,3,2,5,6,7,2,5,5], 9))
# print(s.largestNumber([5,4,4,5,5,5,5,5,5], 19))
print(s.largestNumber([7,6,5,5,5,6,8,7,8], 12))