class TimeMap:

    def __init__(self):
        self.dic = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = []
        self.dic[key].append((value, timestamp))  # Store as a tuple for clarity
    def get(self, key: str, timestamp: int) -> str:
        if(not key in self.dic):
            return ""
        l,r = 0,len(self.dic[key])-1
        if(self.dic[key][0][1]>timestamp):
            return ""
        val = self.dic[key]
        while(l<=r):
            mid = (r-l)//2+l
            if(val[mid][1]==timestamp):
                return self.dic[key][mid][0]
            if(val[mid][1]<timestamp):
                l = mid+1

            else:
                r = mid -1
        return self.dic[key][r][0]
        # while(not timestamp in self.sett and timestamp>0):
        #     print(timestamp)
        #     if(timestamp<self.arr[0][-1]):
        #         break
        #     timestamp -=1
        
        # l,r = 0, len(self.arr)-1
        # while(l<=r):
        #     mid = (r-l)//2+l
        #     if(self.arr[mid][-1]==timestamp):
        #         return self.arr[mid][1]
        #     if(self.arr[mid][-1]<timestamp):
        #         l=mid+1
        #     if(self.arr[mid][-1]>timestamp):
        #         r=mid-1
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)