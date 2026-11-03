class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = []
        d = {}
        for i in range(len(strs)):
            sorted_word = ''.join(sorted(strs[i]))
            if sorted_word in d:
                l[d[sorted_word]].append(strs[i])
            else:
                l.append([strs[i]])
                d[sorted_word] = len(l) - 1
        return l
