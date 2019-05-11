981. Time Based Key-Value Store

Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append(value)
        self.times[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        # 构建一个带有时间版本的KV存储器
        # 查询的时候给出一个时间，要求找到先于(或等于）该时间的最新的key对应的value。
        i = bisect.bisect(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

