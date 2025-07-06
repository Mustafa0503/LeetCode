class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found_a, found_b, found_c = False, False, False
        x, y, z = target

        for a, b, c in triplets:
            if a > x or b > y or c > z:
                continue 

            if a == x:
                found_a = True
            if b == y:
                found_b = True
            if c == z:
                found_c = True
        
        return found_a and found_b and found_c