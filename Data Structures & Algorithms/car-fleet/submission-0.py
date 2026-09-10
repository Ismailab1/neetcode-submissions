class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of tuples from position and speed, pairing each car's position with its speed
        pair = [(p, s) for p, s in zip(position, speed)]
        # Sort the list of pairs in descending order by position
        pair.sort(reverse = True)

        # Initialize a stack to keep track of car fleets
        stack = []

        # Iterate through each car in the sorted list
        for p, s in pair:
            # Calculate the time it takes for the car to reach the target and add it to the stack
            stack.append((target - p) / s)
            # If the last two cars in the stack form a fleet (the last car reaches target at same or later time than the second last car), pop the last car's time
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        # The number of elements in the stack represents the number of car fleets
        return len(stack)
