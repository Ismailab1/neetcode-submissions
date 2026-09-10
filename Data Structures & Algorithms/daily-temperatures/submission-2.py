class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Each index has the amount of days til a hotter temp
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        # Store the temp and index to the stack then
        # only pop when we reach a temp higher than the previous
        # temperature
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])
        
        return res