class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth_list = []
        for i in range (len(accounts)):
            wealth = 0
            for j in accounts[i]:
                wealth = wealth + j
            wealth_list.append(wealth)
        return max(wealth_list)

    # def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(a) for a in accounts)