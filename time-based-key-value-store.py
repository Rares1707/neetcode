class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        my_list = self.store[key]
        start, end = 0, len(my_list) - 1

        answer = ""
        while start <= end:
            mid = (start + end) // 2
            pair = my_list[mid]

            if pair[1] <= timestamp:
                answer = pair[0]
                start = mid + 1
            else:
                end = mid - 1

        return answer
