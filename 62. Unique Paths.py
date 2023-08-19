class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Initialize a dp array of size m+1, n+1 ( extra row and col for '0' padding)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        # Set the last element (finish element) as 1 which acts as the base case for bottom up DP
        dp[m-1][n-1] = 1

        # Traverse the array (without padding) from last to first 
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                #This line makes sure that we dont edit the base case dp[m-1][n-1] = 1
                if(i!=m-1 or j!=n-1):
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        # return the first cell as it contains the sum of all unique paths
        return dp[0][0]

    