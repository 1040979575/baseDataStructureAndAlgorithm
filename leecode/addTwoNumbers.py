class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        sum = ListNode(0)
        temp = sum
        while l1 or l2:
            if l1 == None:
                sum.val = l2.val + sum.val
            elif l2 == None:
                sum.val = l1.val + sum.val
            else:
                sum.val = l1.val + l2.val + sum.val
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            sum.next = ListNode(0)
            pre = sum
            if sum.val < 10:
                sum = sum.next
            else:
                sum.val = sum.val - 10
                sum = sum.next
                sum.val = 1
            if l1 == None and l2 == None and sum.val == 0:
                pre.next = None

        return temp


if __name__ == '__main__':
    aa = Solution()
    aa.addTwoNumbers()
