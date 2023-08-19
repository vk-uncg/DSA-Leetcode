class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        curr_length = len(s)-1
        length = len(s)-1
        mid = int(length/2)
        while(curr_length>mid):
            temp = s[length-curr_length]
            s[length-curr_length] = s[curr_length]
            s[curr_length] = temp
            curr_length -= 1