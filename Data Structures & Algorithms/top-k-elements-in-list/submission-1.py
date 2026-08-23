class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        freq_arr = [[] for i in range(len(nums) + 1)]
        for key in freq_map:
            index = freq_map[key]
            freq_arr[index].append(key)
        ans = []
        for i in range(len(freq_arr) - 1, -1, -1):
            vals = freq_arr[i]
            for val in vals:
                ans.append(val)
                k -= 1
                if k == 0:
                    return ans
        return ans