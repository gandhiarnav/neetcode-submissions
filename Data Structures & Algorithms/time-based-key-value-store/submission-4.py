class TimeMap:

    def __init__(self):
        hashTable =  {}
        self.hashTable = hashTable


    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.hashTable:
            self.hashTable[key] = []

        self.hashTable[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashTable:
            return ""
        arr = self.hashTable[key]
        # print(arr)

        l = 0
        r = len(arr)-1
        ans = ""
        while l<=r:
            mid = (r+l)//2
            if arr[mid][0]<= timestamp:
                ans = arr[mid][1]
                l = mid+1
            else:
                r = mid-1

        return ans


        
        
