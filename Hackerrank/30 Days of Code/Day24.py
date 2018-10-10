class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while start.next != None:
                start = start.next
            start.next = p
        return head

    def display(self, head):
        cur = head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next

    def removeDuplicates(self, head):
        node = head
        while node:
            if node.next:
                if node.data == node.next.data:
                    node.next = node.next.next
                else:
                    node = node.next
            else:
                node = node.next
        return head

if __name__ == '__main__':
    mylist = Solution()
    T = int(input())
    head = None
    for i in range(T):
        data = int(input())
        head = mylist.insert(head, data)
    head = mylist.removeDuplicates(head)
    mylist.display(head)