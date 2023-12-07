import random

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    lists = ListNode()
    current = lists

    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2

        return lists.next
