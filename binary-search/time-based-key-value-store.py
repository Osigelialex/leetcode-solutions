class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(value, timestamp)]
        else:
            self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.map.get(key)
        if not timestamps:
            return ""

        n = len(timestamps)
        L, R = 0, n - 1
        while L <= R:
            mid = (L + R) // 2
            value = timestamps[mid]
            if value[1] == timestamp:
                return value[0]
            elif value[1] < timestamp:
                L = mid + 1
            else:
                R = mid - 1

        prev = timestamps[L - 1]
        if prev[1] > timestamp:
            return ""
        return prev[0]