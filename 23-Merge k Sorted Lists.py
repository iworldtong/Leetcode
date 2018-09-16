# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists is None or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        else:
            L_lists = lists[0 : len(lists)//2]
            R_lists = lists[len(lists)//2 :]
            L_node = self.mergeKLists(L_lists)
            R_node = self.mergeKLists(R_lists)        	                
            return self.merge2Lists(L_node, R_node)

    def merge2Lists(self, node1, node2):    
        node_list = []
        
        while node1 is not None and node2 is not None:            
            if node1.val <= node2.val:
                node_list.append(ListNode(node1.val))
                node1 = node1.next
                
            else:
                node_list.append(ListNode(node2.val))
                node2 = node2.next

        while node1 is not None:
            node_list.append(ListNode(node1.val))
            node1 = node1.next   

        while node2 is not None:
            node_list.append(ListNode(node2.val))
            node2 = node2.next            


        for i in range(len(node_list)-1):
            node_list[i].next = node_list[i+1]

        return node_list[0] if len(node_list) > 0 else None