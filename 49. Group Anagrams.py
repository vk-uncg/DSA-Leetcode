class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = collections.defaultdict(list)
        for word in strs:
            sol[tuple(sorted(word))].append(word)
        return sol.values()
        