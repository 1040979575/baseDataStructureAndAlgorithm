# -*- coding: UTF-8 -*-
# Definition for singly-linked list.

import demo0709

demo0709.greet("yyh")


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_num(ls1, ls2):
    tmp = ListNode(0)
    res = tmp
    while ls1 and ls2:
        tmp.val = ls1.val + ls2.val
        ls1 = ls1.next
        ls2 = ls2.next
        tmp = tmp.next
    return res


