class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1',   '2','3', '4', '5', '6', '7', '8', '9'        ]
        l = 0
        r = len(s)-1
        while l < r:
            print(s[l].lower())
            print(s[l].lower() in alphanumeric)
            while l < len(s) and s[l].lower() not in alphanumeric:
                l += 1
            if l >= len(s):
                # l is out of bounds
                break
            while r >= 0 and s[r].lower() not in alphanumeric:
                r -= 1
            if r < 0:
                # r is out of bounds
                break

            if s[l].lower() != s[r].lower():
                print(s[l])
                print(s[r])
                return False
            l += 1
            r -= 1

        return True
            