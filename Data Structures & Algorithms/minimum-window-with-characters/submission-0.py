class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_freq = {}
        window = {}

        for c in t:
            t_freq[c] = t_freq.get(c, 0) + 1

        have, need = 0, len(t_freq)

        res = [-1, -1]
        resLen = float('inf')

        lp = 0

        for rp in range(len(s)):
            c = s[rp]
            window[c] = window.get(c, 0) + 1

            if c in t_freq and window[c] == t_freq[c]:
                have += 1
            
            while have == need:
                window_size = rp - lp + 1

                if window_size < resLen:
                    res = [lp, rp]
                    resLen = window_size
                
                left_char = s[lp]
                window[left_char] -= 1
            
                if left_char in t_freq and window[left_char] < t_freq[left_char]:
                    have -= 1
                
                lp += 1

        l, r = res
        return s[l:r + 1] if resLen != float('inf') else ""