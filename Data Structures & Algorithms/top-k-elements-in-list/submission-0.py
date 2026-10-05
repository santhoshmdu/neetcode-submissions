class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Count frequency
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        # Sort by frequency
        sorted_count = sorted(count, key=count.get, reverse=True)

        # Return top k numbers
        return sorted_count[:k]