class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort the two strigs that are the same length and have a pointer to each and verify 
        # its the same character and if not return false
        if len(s) == len(t):
            s_sort = ''.join(sorted(s))
            t_sort = ''.join(sorted(t))
            s_pointer = ""
            t_pointer = ""
            for i in range(len(s)):
                t_pointer = t_sort[i]
                s_pointer = s_sort[i]
                print(t_pointer)
                print(s_pointer)
                if t_pointer != s_pointer:
                    return False
            return True
        return False