class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        # Stores the encoded string following this format:
        # regular char -> directly to string
        # / -> string end
        for word in strs:
            for c in word:
                output += c
            output += "/"
        
        return output

    def decode(self, s: str) -> List[str]:
        # Store temp strings into the list
        # once the for loop reaches a "/"
        res = []
        temp = ""
        for i in range(len(s)):
            if s[i] == "/":
                res.append(temp)
                temp = ""
            else:
                temp += s[i]

        # Returns the decoded string   
        return res
