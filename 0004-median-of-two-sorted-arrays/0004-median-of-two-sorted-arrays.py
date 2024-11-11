class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = []
        i=0
        j=0
        while i < len(nums1) and j<len(nums2):
            if(nums1[i]<=nums2[j]):
                a.append(nums1[i])
                i+=1
            else:
                a.append(nums2[j])
                j+=1
            
        while(i<len(nums1)):
            a.append(nums1[i])
            i+=1
        while(j<len(nums2)):
            a.append(nums2[j])
            j+=1
        if len(a) % 2 != 0:
            return a[len(a)//2]
        else:
           
            return (float(a[len(a)//2] + a[len(a)//2 - 1]))/2