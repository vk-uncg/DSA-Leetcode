class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        new_text = ""
        for character in s:
            if character.isalnum():
                new_text += character
        new_text = new_text.lower()
        reverse_text = ""
        for i in range(len(new_text)-1, -1, -1):
            reverse_text += new_text[i]
        return new_text == reverse_text