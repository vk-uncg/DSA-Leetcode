class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        def dp(cur_i, cur_j, k):
            if(cur_i, cur_j, k) in memo:
                return memo[(cur_i, cur_j, k)]
            if pre_sum[cur_i][cur_j] == 0:
                return 0            
            if k == 0:
                return 1   
            
            ans = 0
            for i in range(cur_i+1, m):
                if pre_sum[cur_i][cur_j] - pre_sum[i][cur_j] > 0:
                     ans += dp(i, cur_j, k-1)
                
            for j in range(cur_j+1, n):
                if pre_sum[cur_i][cur_j] - pre_sum[cur_i][j] > 0:
                    ans += dp(cur_i,j,k-1)            
            memo[(cur_i, cur_j, k)] = ans
            
            return ans                        
        memo = {}
        
        m = len(pizza)
        n = len(pizza[0])                
        pre_sum = [[0]*(n+1) for _ in range(m+1)]        
        for i in range(m-1,-1,-1):
            for j in range(n-1, -1, -1):
                pre_sum[i][j] = pre_sum[i][j+1] + pre_sum[i+1][j] - pre_sum[i+1][j+1] + (1 if pizza[i][j] =='A' else 0)
        
        return dp(0,0,k-1) % (10**9 + 7)
        