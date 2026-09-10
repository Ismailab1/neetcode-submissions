class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) # 0-indexed array
        stack = [] #pair of index and value
        for index, temp in enumerate(temperatures): # tracks the index and the current temperature
            while stack and stack[-1][0] < temp: # while there are temperatures lower than the current temp
                stackTemp, stackIndex = stack.pop() # pops the top temperature and the index of that tempaeature
                result[stackIndex] = index - stackIndex # stores the difference between the current day and the colder day
            stack.append([temp, index]) # appends the current temperature and day to compare when a hotter day comes forward
        return result # returns the result