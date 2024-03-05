class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = len(s) - 1
        while left <= right:
            if (right == left): return 1
            l = s[left]
            r = s[right]
            if (l != r):
                break
            while left <= right and s[left] == l:
                left += 1
            while left <= right and s[right] == r:
                right -= 1
        return right - left + 1
    
solution = Solution()

# print(solution.minimumLength("ca"))
# print(solution.minimumLength("cabaabac"))
# print(solution.minimumLength("aabccabba"))
print(solution.minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"))
