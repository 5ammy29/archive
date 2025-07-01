class ListNode():

    def  __init__(self, val: int) -> None:
        self.val = val
        self.prev = None
        self.next = None

class CircularLinkedList():

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push(self, val: int) -> None:     # O(1)
        node = ListNode(val)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        if self.head and self.tail:
            self.head.prev = self.tail
            self.tail.next = self.head
        
    def insert(self, index: int, val: int) -> None:     # O(index)
        if index <= 0 or not self.head:
            self.push(val)
            return None
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
            if curr == self.head:
                break
        node = ListNode(val)
        node.next = curr.next
        node.prev = curr
        curr.next.prev = node
        curr.next = node
        if curr == self.tail:
            self.tail = node
        if self.head and self.tail:
            self.head.prev = self.tail
            self.tail.next = self.head

    def append(self, val: int) -> None:     # O(1)
        node = ListNode(val)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        if self.head and self.tail:
            self.head.prev = self.tail
            self.tail.next = self.head

    def pop(self) -> int | None:     # O(1)
        if not self.tail:
            return None
        val = self.tail.val
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        return val

    def delete(self, index: int) -> None:     # O(index)
        if index < 0 or not self.head:
            return None
        if self.head == self.tail:
            self.head = self.tail = None
            return None
        if index == 0:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.next
            if curr == self.head:
                return None
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        if curr == self.tail:
            self.tail = curr.prev

    def remove(self, val: int) -> None:     # O(n)
        if not self.head:
            return None
        curr = self.head
        while True:
            if curr.val == val:
                if curr == self.head:
                    self.head = curr.next
                if curr == self.tail:
                    self.tail = curr.prev
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                if self.head and self.tail:
                    self.head.prev = self.tail
                    self.tail.next = self.head
                return None
            curr = curr.next
            if curr == self.head:
                break

    def replace(self, index: int, val: int) -> None:     # O(index)
        if index < 0:
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.next
            if curr == self.head:
                return None
        curr.val = val

    def peek(self) -> int | None:     # O(1)
        if self.head:
            return self.head.val
        else:
            return None

    def get(self, index: int) -> int | None:     # O(index)
        if index < 0 or not self.head:
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.next
            if curr == self.head:
                return None
        return curr.val

    def show(self) -> str:     # O(n)
        if not self.head:
            return ""
        result = []
        curr = self.head
        while True:
            result.append(str(curr.val))
            curr = curr.next
            if curr == self.head:
                break
        return " -> ".join(result) + " -> (head)"

    def contains(self, val: int) -> bool:     # O(n)
        if not self.head:
            return False
        curr = self.head
        while True:
            if curr.val == val:
                return True
            curr = curr.next
            if curr == self.head:
                break
        return False

    def is_empty(self) -> bool:     # O(1)
        if self.head:
            return False
        else:
            return True

    def size(self) -> int:     # O(n)
        if not self.head:
            return 0
        curr = self.head
        count = 0
        while True:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        return count

    def reverse(self) -> None:     # O(n)
        if not self.head or self.head == self.tail:
            return None
        curr = self.head
        while True:
            curr.prev, curr.next = curr.next, curr.prev
            curr = curr.prev
            if curr == self.head:
                break
        self.head, self.tail = self.tail, self.head
        if self.head and self.tail:
            self.head.prev = self.tail
            self.tail.next = self.head

    def sort(self) -> None:     # O(nlogn)
        if not self.head or self.head == self.tail:
            return None
        self.tail.next = None
        self.head.prev = None
        self.head = self._merge_sort(self.head)
        curr = self.head
        while curr.next:
            curr = curr.next
        self.tail = curr
        self.tail.next = self.head
        self.head.prev = self.tail

    def _merge_sort(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        mid = self._get_middle(head)
        right = mid.next
        mid.next = None
        if right:
            right.prev = None
        left = self._merge_sort(head)
        right = self._merge_sort(right)
        return self._merge(left, right)

    def _get_middle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
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
        elif right_sorted:
            tail.next = right_sorted
            right_sorted.prev = tail
        result = dummy.next
        if result:
            result.prev = None
        return result
    
# --------------- Tests ---------------

def test_push():
    ll = CircularLinkedList()
    ll.push(10)
    ll.push(20)
    ll.push(30)
    assert ll.show() == "30 -> 20 -> 10 -> (head)"

def test_insert():
    ll = CircularLinkedList()
    ll.append(10)
    ll.append(30)
    ll.insert(1, 20)
    assert ll.show() == "10 -> 20 -> 30 -> (head)"
    ll.insert(0, 0)
    assert ll.show() == "0 -> 10 -> 20 -> 30 -> (head)"

def test_append():
    ll = CircularLinkedList()
    ll.append(10)
    ll.append(20)
    assert ll.show() == "10 -> 20 -> (head)"

def test_pop():
    ll = CircularLinkedList()
    assert ll.pop() is None
    ll.append(10)
    ll.append(20)
    ll.append(30)
    assert ll.pop() == 30
    assert ll.show() == "10 -> 20 -> (head)"

def test_delete():
    ll = CircularLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.delete(1)
    assert ll.show() == "10 -> 30 -> 40 -> (head)"

def test_remove():
    ll = CircularLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.remove(20)
    assert ll.show() == "10 -> 30 -> (head)"
    ll.remove(10)
    assert ll.show() == "30 -> (head)"
    ll.remove(40) 
    assert ll.show() == "30 -> (head)"

def test_replace():
    ll = CircularLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.replace(1, 40)
    assert ll.show() == "10 -> 40 -> 30 -> (head)"
    ll.replace(4, 5) 
    assert ll.show() == "10 -> 40 -> 30 -> (head)"

def test_peek():
    ll = CircularLinkedList()
    assert ll.peek() is None
    ll.append(10)
    assert ll.peek() == 10  

def test_get():
    ll = CircularLinkedList()
    ll.append(10)
    ll.append(20)
    assert ll.get(0) == 10
    assert ll.get(1) == 20
    assert ll.get(2) is None
    assert ll.get(-1) is None

def test_show():
    ll = CircularLinkedList()
    assert ll.show() == ""
    ll.append(10)
    ll.append(20)
    assert ll.show() == "10 -> 20 -> (head)"

def test_contains():
    ll = CircularLinkedList()
    ll.append(10)
    ll.append(20)
    assert ll.contains(10) is True
    assert ll.contains(30) is False

def test_is_empty():
    ll = CircularLinkedList()
    assert ll.is_empty() is True
    ll.append(10)
    assert ll.is_empty() is False

def test_size():
    ll = CircularLinkedList()
    assert ll.size() == 0
    ll.append(10)
    ll.append(20)
    assert ll.size() == 2

def test_reverse():
    ll = CircularLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.reverse()
    assert ll.show() == "30 -> 20 -> 10 -> (head)"

def test_sort():
    ll = CircularLinkedList()
    ll.append(40)
    ll.append(30)
    ll.append(20)
    ll.append(10)
    ll.sort()
    assert ll.show() == "10 -> 20 -> 30 -> 40 -> (head)"