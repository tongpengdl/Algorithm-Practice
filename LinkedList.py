from ListNode import ListNode


class LinkedList:
    """
    LikedList geeks for geeks algorithm practice
    """
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    # 16. reverse a linkedList, iterative
    def reverse_iter(self, head):
        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    # 16. reverse a linkedList, recursive
    def reverse_rec(self, head):
        

if __name__ == "__main__":
    pass
