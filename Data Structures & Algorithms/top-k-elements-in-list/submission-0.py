class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = [[] for i in range(len(nums) + 1)]
        freq_dict = {}

        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)

        for num, count in freq_dict.items():
            freq_list[count].append(num)

        result = []
        for i in range(len(freq_list) - 1, 0, -1):
            vals = freq_list[i]
            for val in vals:
                result.append(val)
                k -= 1
                if k == 0:
                    return result
        return result

        