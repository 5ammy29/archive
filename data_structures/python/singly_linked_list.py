class ListNode:

    def __init__(self, val: int) -> None:
        self.val = val
        self.prev = None
        self.next = None

class SinglyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push(self, val: int) -> None:     # O(1)
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def insert(self, index: int, val: int) -> None:     # O(index)   
        node = ListNode(val)
        if index <= 0 or not self.head:
            node.next = self.head
            self.head = node
            return None
        curr = self.head
        for i in range(index - 1):
            if not curr.next: 
                break
            curr = curr.next
        node.next = curr.next
        curr.next = node

    def append(self, val: int) -> None:     # O(n)
        node = ListNode(val)
        if not self.head: 
            self.head = node
            return None
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def pop(self) -> int | None:     # O(n)
        if not self.head:
            return None  
        if not self.head.next:
            val = self.head.val  
            self.head = None
            return val
        prev = self.head
        curr = self.head.next
        while curr.next:
            prev = curr
            curr = curr.next
        val = curr.val
        prev.next = None
        return val
    
    def delete(self, index: int) -> None:     # O(index)
        if index < 0 or not self.head:
            return None
        if index == 0:
            self.head = self.head.next
            return None
        curr = self.head
        for i in range(index - 1):
            if not curr.next:
                return None
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next

    def remove(self, val: int) -> None:     # O(n)
        if self.head and self.head.val == val:
            self.head = self.head.next
            return None
        curr = self.head
        while curr and curr.next and curr.next.val != val:
            curr = curr.next
        if curr.next and curr.next.val == val:
            curr.next = curr.next.next

    def replace(self, index: int, val: int) -> None:     # O(n)
        if index < 0:
            return None
        curr = self.head
        while index > 0 and curr:
            curr = curr.next
            index -= 1
        if curr:
            curr.val = val

    def peek(self) -> int | None:     # O(1)
        if self.head:
            return self.head.val
        else:
            return None

    def get(self, index: int) -> int | None:     # O(index)
        if index < 0:
            return None
        curr = self.head
        while index > 0:
            curr = curr.next
            index -= 1
        if curr:
            return curr.val
        else:
            return None 

    def show(self) -> str:     # O(n)
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        return " -> ".join(elements)
    
    def contains(self, val: int) -> bool:     # O(n)
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next  
        return False
    
    def is_empty(self) -> bool:     # O(1)
        if self.head:
            return False
        else:
            return True

    def size(self) -> int:     # O(n)
        length = 0
        curr = self.head
        while curr:
            curr = curr.next
            length += 1
        return length

    def reverse(self) -> None:     # O(n)
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def sort(self) -> None:     # O(nlogn)
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        mid = self._get_middle(head)
        right = mid.next
        mid.next = None
        left_sorted = self._merge_sort(head)
        right_sorted = self._merge_sort(right)
        return self._merge(left_sorted, right_sorted)

    def _get_middle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, left_sorted: ListNode | None, right_sorted: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        tail = dummy
        while left_sorted and right_sorted:
            if left_sorted.val < right_sorted.val:
                tail.next = left_sorted
                left_sorted = left_sorted.next
            else:
                tail.next = right_sorted
                right_sorted = right_sorted.next
            tail = tail.next
        tail.next = left_sorted or right_sorted
        return dummy.next

# --------------- Tests ---------------

def test_push():
    ll = SinglyLinkedList()
    ll.push(10)
    ll.push(20)
    ll.push(30)
    assert ll.show() == "30 -> 20 -> 10"

def test_insert():
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(30)
    ll.insert(1, 20)
    assert ll.show() == "10 -> 20 -> 30"
    ll.insert(0, 0)
    assert ll.show() == "0 -> 10 -> 20 -> 30"

def test_append():
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    assert ll.show() == "10 -> 20"

def test_pop():
    ll = SinglyLinkedList()
    assert ll.pop() is None
    ll.append(10)
    ll.append(20)
    ll.append(30)
    assert ll.pop() == 30
    assert ll.show() == "10 -> 20"

def test_delete():
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.delete(1)
    assert ll.show() == "10 -> 30 -> 40" 

def test_remove():
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.remove(20)
    assert ll.show() == "10 -> 30"
    ll.remove(10)
    assert ll.show() == "30"
    ll.remove(40) 
    assert ll.show() == "30"

def test_replace():
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.replace(1, 40)
    assert ll.show() == "10 -> 40 -> 30"
    ll.replace(10, 5) 
    assert ll.show() == "10 -> 40 -> 30"

def test_peek():
    ll = SinglyLinkedList()
    assert ll.peek() is None
    ll.append(10)
    assert ll.peek() == 10

def test_get():
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    assert ll.get(0) == 10
    assert ll.get(1) == 20
    assert ll.get(2) is None
    assert ll.get(-1) is None

def test_show():
    ll = SinglyLinkedList()
    assert ll.show() == ""
    ll.append(10)
    ll.append(20)
    assert ll.show() == "10 -> 20"

def test_contains():
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    assert ll.contains(10) is True
    assert ll.contains(30) is False

def test_is_empty():
    ll = SinglyLinkedList()
    assert ll.is_empty() is True
    ll.append(10)
    assert ll.is_empty() is False

def test_size():
    ll = SinglyLinkedList()
    assert ll.size() == 0
    ll.append(10)
    ll.append(20)
    assert ll.size() == 2

def test_reverse():
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.reverse()
    assert ll.show() == "30 -> 20 -> 10"

def test_sort():
    ll = SinglyLinkedList()
    ll.append(40)
    ll.append(30)
    ll.append(20)
    ll.append(10)
    ll.sort()
    assert ll.show() == "10 -> 20 -> 30 -> 40"