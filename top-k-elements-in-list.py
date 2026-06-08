class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for number in nums:
            counts[number] += 1

        frequency = [[] for _ in range(len(nums) + 1)]

        for number, count in counts.items():
            frequency[count].append(number)

        result = []
        i = len(nums)
        while len(result) < k:
            if len(frequency[i]):
                result.append(frequency[i][-1])
                frequency[i].pop()
            else:
                i -= 1
        return result
