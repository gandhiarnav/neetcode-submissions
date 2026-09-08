class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        # print(candidates)
        def dfs(i,cur_sum,arr):
            if cur_sum == target:
                res.append(arr.copy())
                # print(arr)
                return
            elif i >= len(candidates) or cur_sum > target:
                return

            next_i = i+1
            while next_i < len(candidates) and candidates[next_i] == candidates[next_i-1]:
                next_i +=1

            dfs(next_i,cur_sum,arr)

            arr.append(candidates[i])
            # print(arr)
            cur_sum+=candidates[i]

            dfs(i+1,cur_sum,arr)
            arr.pop()
            cur_sum-= candidates[i]


        dfs(0,0,[])

        return res
