class TimeMap:

    def __init__(self):
        self.time_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_dict:
            return ""
        
        result = ""
        values = self.time_dict[key]
        left, right = 0, len(values) - 1
        
        while left <= right:
            mid = left + (right - left) // 2

            if values[mid][1] <= timestamp:
                result = values[mid][0]
                left = mid + 1
            
            else:
                right = mid - 1

        return result
