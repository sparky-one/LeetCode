class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        answer = []
        for i in range (len(nums)):
            sum = sum + nums[i]
            answer.append(sum)
        return answer