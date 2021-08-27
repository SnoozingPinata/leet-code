# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Runtime: 91 ms, faster than 10.25% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.4 MB, less than 44.59% of Python3 online submissions for Add Two Numbers.
class Solution:
    def addTwoNumbers(self, l1, l2):
        val1 = self.evaluate(l1)
        val2 = self.evaluate(l2)
        my_sum = val1 + val2
        return self.convert_to_list_node(my_sum)

    def evaluate(self, list_node):
        if list_node.next == None:
            return list_node.val
        else:
            return list_node.val + (self.evaluate(list_node.next) * 10)

    def convert_to_list_node(self, input):
        iterable = str(input)
        last_val = None
        for char in iterable:
            temp_list_node = ListNode(val=int(char), next=last_val)
            last_val = temp_list_node
        return temp_list_node


l1_3 = ListNode(val=3)
l1_2 = ListNode(val=4, next=l1_3)
l1 = ListNode(val=2, next=l1_2)

l2_3 = ListNode(val=4)
l2_2 = ListNode(val=6, next=l2_3)
l2 = ListNode(val=5, next=l2_2)

sol = Solution()
print(sol.addTwoNumbers(l1, l2))