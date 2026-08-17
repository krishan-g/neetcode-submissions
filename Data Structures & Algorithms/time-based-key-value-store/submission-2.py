from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # key -> [(value, timestamp)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        possible_values = self.store[key]

        l, r = 0, len(possible_values) - 1
        res = None

        while l <= r:
            m = (l + r) // 2

            if possible_values[m][1] > timestamp:
                r = m - 1
            else:
                res = possible_values[m][0]
                l = m + 1
        
        return res if res else ""
