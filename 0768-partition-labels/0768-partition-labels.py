class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #1. find last app of each charecter's index
        last_ind = {}
        for i in range(len(s)):
            last_ind[s[i]] = i
        #2. partition
        partition = []
        start, end = 0,0
        for i in range(len(s)):
            end = max(end, last_ind[s[i]])
            # if we reach end of the parition 
            if i==end:
                partition.append(i-start+1)
                start = i+1
        return partition
        

