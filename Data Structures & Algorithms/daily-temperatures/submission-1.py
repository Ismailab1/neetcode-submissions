class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)): # iterates the index of the current day
            while stack and temperatures[stack[-1]] < temperatures[i]: # checks if the temperature on the day that the top of the stack has is less than the current day
                j = stack.pop() # pops the index fo teh colder day
                result[j] = i - j # stores the difference between the days in at the popped day
            stack.append(i) # appends the current index for future comparison
        return result