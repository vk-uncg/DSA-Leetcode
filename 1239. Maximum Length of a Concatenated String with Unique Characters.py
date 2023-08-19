class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = ['']
        maxlen = ""

        for i in range(len(arr)):
            for j in range(len(dp)):
                temp_string = arr[i]+dp[j]
                if(len(temp_string)==len(set(temp_string))):
                    dp.append(temp_string)
        maxlen = max(dp, key = len)
        return len(maxlen)
        