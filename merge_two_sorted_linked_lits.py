import random

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    # Create a dummy node to simplify the code
    lists = ListNode()
    current = lists