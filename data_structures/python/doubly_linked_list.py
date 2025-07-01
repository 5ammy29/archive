class ListNode:

    def __init__(self, val: int) -> None:
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push(self, val: int) -> None:     # O(1)
        node = ListNode(val)
        node.next = self.head
        if self.head:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node

    def insert(self, index: int, val: int) -> None:     # O(index)
        node = ListNode(val)
        if index <= 0 or not self.head:
            self.push(val)
            return None
        curr = self.head
        for i in range(index - 1):
            if not curr.next:
                break
            curr = curr.next
        node.next = curr.next
        node.prev = curr
        if curr.next:
            curr.next.prev = node
        else:
            self.tail = node
        curr.next = node

    def append(self, val: int) -> None:     # O(1)
        node = ListNode(val)
        if not self.head:
            self.head = self.tail = node
            return None
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def pop(self) -> int | None:     # O(1)
        if not self.tail:
            return None
        val = self.tail.val
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return val

    def delete(self, index: int) -> None:     # O(index)
        if index < 0 or not self.head:
            return None
        if index == 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return None
        curr = self.head
        for i in range(index):
            if not curr:
                return None
            curr = curr.next
        if not curr:
            return None
        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev
        if curr.prev:
            curr.prev.next = curr.next

    def remove(self, val: int) -> None:     # O(n)
        curr = self.head
        while curr:
            if curr.val == val:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                return None
            curr = curr.next

    def replace(self, index: int, val: int) -> None:     # O(index)
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
        while index > 0 and curr:
            curr = curr.next
            index -= 1
        if curr:
            return curr.val
        else:
            return None

    def show(self) -> str:     # O(n)
        curr = self.head
        result = []
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        return " <-> ".join(result)
    
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
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def reverse(self) -> None:     # O(n)
        curr = self.head
        prev = None
        while curr:
            prev = curr.prev
            curr.prev = curr.next
            curr.next = prev
            curr = curr.prev
        if prev:
            self.head, self.tail = self.tail, self.head

    def sort(self) -> None:     # O(nlogn)
        self.head = self._merge_sort(self.head)
        curr = self.head
        prev = None
        while curr:
            prev = curr
            curr = curr.next
        self.tail = prev

    def _merge_sort(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        middle = self._get_middle(head)
        right = middle.next
        middle.next = None
        if right:
            right.prev = None
        left_sorted = self._merge_sort(head)
        right_sorted = self._merge_sort(right)
        return self._merge(left_sorted, right_sorted)

    def _get_middle(self, node: ListNode) -> ListNode:
        slow = node
        fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, left_sorted: ListNode | None, right_sorted: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        tail = dummy
        while left_sorted and right_sorted:
            if left_sorted.val < right_sorted.val:
                tail.next = left_sorted
                left_sorted.prev = tail
                left_sorted = left_sorted.next
            else:
                tail.next = right_sorted
                right_sorted.prev = tail
                right_sorted = right_sorted.next
            tail = tail.next
        if left_sorted:
            tail.next = left_sorted
            left_sorted.prev = tail
        if right_sorted:
            tail.next = right_sorted
            right_sorted.prev = tail
        dummy.next.prev = None
        return dummy.next

# --------------- Tests ---------------

def test_push():
    ll = DoublyLinkedList()
    ll.push(10)
    ll.push(20)
    ll.push(30)
    assert ll.show() == "30 <-> 20 <-> 10"

def test_insert():
    ll = DoublyLinkedList()
    ll.append(10)
    ll.append(30)
    ll.insert(1, 20)
    assert ll.show() == "10 <-> 20 <-> 30"
    ll.insert(0, 0)
    assert ll.show() == "0 <-> 10 <-> 20 <-> 30"

def test_append():
    ll = DoublyLinkedList()
    ll.append(10)
    ll.append(20)
    assert ll.show() == "10 <-> 20"

def test_pop():
    ll = DoublyLinkedList()
    assert ll.pop() is None
    ll.append(10)
    ll.append(20)
    ll.append(30)
    assert ll.pop() == 30
    assert ll.show() == "10 <-> 20"

def test_delete():
    ll = DoublyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.delete(1)
    assert ll.show() == "10 <-> 30 <-> 40" 

def test_remove():
    ll = DoublyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.remove(20)
    assert ll.show() == "10 <-> 30"
    ll.remove(10)
    assert ll.show() == "30"
    ll.remove(4) 
    assert ll.show() == "30"

def test_replace():
    ll = DoublyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.replace(1, 40)
    assert ll.show() == "10 <-> 40 <-> 30"
    ll.replace(4, 5) 
    assert ll.show() == "10 <-> 40 <-> 30"

def test_peek():
    ll = DoublyLinkedList()
    assert ll.peek() is None
    ll.append(1)
    assert ll.peek() == 1

def test_get():
    ll = DoublyLinkedList()
    ll.append(10)
    ll.append(20)
    assert ll.get(0) == 10
    assert ll.get(1) == 20
    assert ll.get(2) is None
    assert ll.get(-1) is None

def test_show():
    ll = DoublyLinkedList()
    assert ll.show() == ""
    ll.append(10)
    ll.append(20)
    assert ll.show() == "10 <-> 20"

def test_contains():
    ll = DoublyLinkedList()
    ll.append(10)
    ll.append(20)
    assert ll.contains(10) is True
    assert ll.contains(30) is False

def test_is_empty():
    ll = DoublyLinkedList()
    assert ll.is_empty() is True
    ll.append(10)
    assert ll.is_empty() is False

def test_size():
    ll = DoublyLinkedList()
    assert ll.size() == 0
    ll.append(10)
    ll.append(20)
    assert ll.size() == 2

def test_reverse():
    ll = DoublyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.reverse()
    assert ll.show() == "30 <-> 20 <-> 10"

def test_sort():
    ll = DoublyLinkedList()
    ll.append(40)
    ll.append(30)
    ll.append(20)
    ll.append(10)
    ll.sort()
    assert ll.show() == "10 <-> 20 <-> 30 <-> 40"