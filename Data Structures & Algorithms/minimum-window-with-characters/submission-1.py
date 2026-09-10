class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        s_counter = Counter()

        left = 0

        min_substring = ""
        min_substring_length = 1001

        for right in range(len(s)):
            if s[right] in t:
                s_counter[s[right]] += 1
            
            while all(s_counter[char] >= count for char, count in t_counter.items()):
                if right - left + 1 < min_substring_length:
                    min_substring_length = right - left + 1
                    min_substring = s[left:right+1]
                if s[left] in t:
                    s_counter[s[left]] -= 1
                left += 1
        
        return min_substring