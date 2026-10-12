class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_set = set(nums)
        longest = 0

        for num in number_set:
            # Start only from the first number of a sequence
            if num - 1 not in number_set:
                current = num
                length = 1

                while current + 1 in number_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest