# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:  # Edge case: If lists is empty, return None
            return None

        head = ListNode(0)  # Temporary head node
        l3 = head           # Pointer for building the merged list
        
        # Initialize l1 to the first list, or set it to None if lists[0] is empty
        l1 = lists[0] if lists[0] is not None else None

        # Iterate over the lists, merging them one by one
        for i in range(1, len(lists)):
            l2 = lists[i]
            l3 = head  # Reset l3 to the start of the merged list for each iteration

            # Merge l1 and l2 into l3
            while l1 is not None and l2 is not None:
                if l1.val <= l2.val:
                    l3.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    l3.next = ListNode(l2.val)
                    l2 = l2.next
                l3 = l3.next

            # Attach remaining nodes in either l1 or l2
            if l1 is not None:
                l3.next = l1
            elif l2 is not None:
                l3.next = l2

            # Move l1 to the new merged list (head.next) for the next iteration
            l1 = head.next
            head.next = None  # Reset head for the next merge

            # Print merged list after each merge (for debugging)
            yo = l1


        return l1  # l1 now holds the fully merged list
