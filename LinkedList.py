from ListNode import ListNode


def printList(head):
    temp = head
    while temp is not None:
        print temp.val,
        temp = temp.next


# 16. reverse a linkedList, iterative
def reverse_iter(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


# 16. reverse a linkedList, recursive
def reverse_rec(head):
    if head is None or head.next is None:
        return head
    next = head.next
    new_head = reverse_rec(next)
    next.next = head
    head.next = None
    return new_head

# 17. detect cycle in linkedlist
# proof: https://www.quora.com/How-does-Floyds-cycle-finding-algorithm-work
def detectloop_flag(head):
    if head is None or head.next is None:
        return "No loop"
    while head is not None and not head.is_visited:
        head.is_visited = True
        head = head.next

    if not head:
        return "No loop"
    else:
        return "find loop"

def detectloop_2pointer(head):
    if head is None or head.next is None:
        return "No loop"

    slow = head
    fast = head
    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

        if fast is slow:
            return "find loop"
    return "No loop"

if __name__ == "__main__":
    l1 = ListNode(20)
    l2 = ListNode(21)
    l3 = ListNode(22)
    l4 = ListNode(23)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l3

    print detectloop_2pointer(l1)
