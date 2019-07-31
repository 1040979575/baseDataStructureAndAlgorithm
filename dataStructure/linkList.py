class Node(object):
    def __init__(self, num):
        self.num = num
        self.next = None


class LinkList(object):
    def __init__(self, num):
        self.head = Node(num)
        self.next = None

    def lenth(self):
        lenth = 0
        temp = self.head
        if self.is_empty():
            return lenth
        while temp is not None:
            lenth += 1
            temp = temp.next

        return lenth

    def is_empty(self):
        return True if self.head is None else False

    def add(self, num):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(num)
        return self.head

    def delete(self, num):
        if self.is_empty():     # 处理为空的情况
            return None

        pre = self.head
        post = pre.next
        if pre.num == num:      # 处理首节点匹配的情况
            self.head = post
        else:
            while post:
                if post.num == num:
                    pre.next = post.next
                    break
                pre = post
                post = post.next
        return self.head

    def reverse(self):  # 逻辑上是对的，但是运行有问题
        if self.lenth() < 2:
            return
        pre = self.head
        post = pre.next
        while post:
            temp = post.next
            post.next = pre
            pre = post
            post = temp
        self.head.next = None
        self.head = pre
        return self.head


if __name__ == '__main__':
    ls = LinkList(0)
    ls.add(1)
    ls.add(2)
    ls.add(3)
    ls.add(4)
    ls.add(5)
    sum = ls.reverse()
    print(sum.lenth())
