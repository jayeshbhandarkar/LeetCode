class Solution:
    def judgePoint24(self, cards):
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    a, b = nums[i], nums[j]

                    results = [a + b, a - b, b - a, a * b]
                    if abs(b) > 1e-6: 
                        results.append(a / b)
                    if abs(a) > 1e-6: 
                        results.append(b / a)

                    new_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]

                    for r in results:
                        if dfs(new_nums + [r]):
                            return True
            return False

        return dfs([float(x) for x in cards])
