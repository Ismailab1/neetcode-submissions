class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return False
        
        s1_chars = Counter(s1)
        print(f"Current set: {s1_chars}")

        l = 0

        for r in range(len(s2)):
            if s2[r] in s1_chars:
                    s1_chars[s2[r]] -= 1
                    print(f"Decremented {s2[r]} from set! New Current set: {s1_chars}")
            
            while r - l + 1 > len(s1):
                if s2[l] in s1_chars:
                    s1_chars[s2[l]] += 1
                    print(f"Incremented {s2[l]} from set! New Current set: {s1_chars}")
                l += 1
            
            if all(x == 0 for x in s1_chars.values()):
                return True
        
        return False