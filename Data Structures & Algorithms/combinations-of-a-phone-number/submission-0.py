class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digitsToChar = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        result = [""]
        for digit in digits:
            temp = []
            for curStr in result:
                for c in digitsToChar[digit]:
                    print(f"Adding {c} to {curStr}")
                    temp.append(curStr + c)
            result = temp
        return result