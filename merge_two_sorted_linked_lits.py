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

def generate_sorted_linked_list(length):
    values = [random.randint(0, 50) for _ in range(length)]
    values.sort()
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list_without_arrow(head):
    current = head
    while current is not None:
        print(current.value, end="")
        current = current.next
        if current is not None:
            print(" -> ", end="")
    print()

if __name__ == "__main__":
    random_list1 = generate_sorted_linked_list(10)
    random_list2 = generate_sorted_linked_list(10)

    print("Random List 1:")
    print_linked_list_without_arrow(random_list1)

    print("\nRandom List 2:")
    print_linked_list_without_arrow(random_list2)

    merged_random_list = merge_sorted_lists(random_list1, random_list2)

    print("\nMerged and Sorted Random List:")
    print_linked_list_without_arrow(merged_random_list)

# Please try the program

