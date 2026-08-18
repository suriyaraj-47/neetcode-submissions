class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        # Count frequency
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Create buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        # Put each number into its frequency bucket
        for num, freq in count.items():
            bucket[freq].append(num)

        result = []

        # Go from highest frequency to lowest
        for freq in range(len(bucket) - 1, 0, -1):

            for num in bucket[freq]:
                result.append(num)

                if len(result) == k:
                    return result