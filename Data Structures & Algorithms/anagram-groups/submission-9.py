class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict()

        for anagram in strs:
            sorted_anagram = "".join(sorted(anagram))

            if sorted_anagram not in anagrams:
                anagrams.setdefault(sorted_anagram, [])
                anagrams[sorted_anagram].append(anagram)
            
            else:
                anagrams[sorted_anagram].append(anagram)

        return list(anagrams.values())