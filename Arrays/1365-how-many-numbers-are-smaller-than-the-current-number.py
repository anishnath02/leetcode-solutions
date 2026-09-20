class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted((nums))
        hashmap = {}

        for idx, val in enumerate(temp):
            if val not in hashmap:
                hashmap[val] = idx
            
        res = []

        for i in nums:
            res.append(hashmap[i])

        return res
