class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # my first solution without looking at solutions/concepts to use
        #
        # for i in range(len(nums)):
        #     for j in range(len(nums)-1):
        #         if i == j+1:
        #             j += 1
        #         if nums[i] + nums[j+1] == target:
        #             return i, j+1

        # my new solution knowing to use a hashmap
        # note for future: dictionaries are like hashmaps, no dupes

        # initialize empty dict
        numsmap = {}

        # for each index in the array
        for i in range(len(nums)):
            complement = target - nums[i]           # find the number that would add up to the target w the current index's value
            if complement in numsmap.keys():        # if that needed value is in the dict
                return [numsmap[complement], i]     # return the pair of the needed value and the current index u check w
            numsmap[nums[i]] = i                    # ELSE if its not in dict, add the pair to the dict
