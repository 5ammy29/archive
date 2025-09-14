#include <iostream>

struct ListNode {
    int val;
    ListNode* next;

    ListNode(int val) {
        this->val = val;
        next = nullptr;
    }
};

class SinglyLinkedList {
    ListNode* head;

public:
    SinglyLinkedList() {
        head = nullptr;
    }

    ~SinglyLinkedList() {
        while (head) {
            ListNode* tmp = head;
            head = head->next;
            delete tmp;
        }
    }

private: 
    ListNode* mergeSort(ListNode* node) {
        if (!node || !node->next) return node;
        ListNode* mid = getMiddle(node);
        ListNode* right = mid->next;
        mid->next = nullptr;
        ListNode* leftSorted = mergeSort(node);
        ListNode* rightSorted = mergeSort(right);
        return merge(leftSorted, rightSorted);
    }

    ListNode* getMiddle(ListNode* node) {
        ListNode* slow = node;
        ListNode* fast = node->next;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }

    ListNode* merge(ListNode* left, ListNode* right) {
        ListNode dummy(0);
        ListNode* tail = &dummy;
        while (left && right) {
            if (left->val < right->val) {
                tail->next = left;
                left = left->next;
            } else {
                tail->next = right;
                right = right->next;
            }
            tail = tail->next;
        }
        tail->next = (left ? left : right);
        return dummy.next;
    }
    
public:
    void push(int val) {     // O(1)
        ListNode* node = new ListNode(val);
        node->next = head;
        head = node;
    }

    void insert(int index, int val) {     // O(index)
        ListNode* node = new ListNode(val);
        if (index <= 0 || !head) {
            node->next = head;
            head = node;
            return;
        }
        ListNode* curr = head;
        for (int i = 0; i < index - 1 && curr->next; i++) {
            curr = curr->next;
        }
        node->next = curr->next;
        curr->next = node;
    }

    void append(int val) {     // O(n)
        ListNode* node = new ListNode(val);
        if (!head) {
            head = node;
            return;
        }
        ListNode* curr = head;
        while (curr->next) curr = curr->next;
        curr->next = node;
    }

    int pop() {     // O(n)
        if (!head) return -1; 
        if (!head->next) {
            int val = head->val;
            delete head;
            head = nullptr;
            return val;
        }
        ListNode* prev = head;
        ListNode* curr = head->next;
        while (curr->next) {
            prev = curr;
            curr = curr->next;
        }
        int val = curr->val;
        delete curr;
        prev->next = nullptr;
        return val;
    }

    void deleteAt(int index) {     // O(index)
        if (index < 0 || !head) return;
        if (index == 0) {
            ListNode* tmp = head;
            head = head->next;
            delete tmp;
            return;
        }
        ListNode* curr = head;
        for (int i = 0; i < index - 1 && curr->next; i++) {
            curr = curr->next;
        }
        if (curr->next) {
            ListNode* tmp = curr->next;
            curr->next = tmp->next;
            delete tmp;
        }
    }

    void remove(int val) {     // O(n)
        if (head && head->val == val) {
            ListNode* tmp = head;
            head = head->next;
            delete tmp;
            return;
        }
        ListNode* curr = head;
        while (curr && curr->next && curr->next->val != val) {
            curr = curr->next;
        }
        if (curr && curr->next) {
            ListNode* tmp = curr->next;
            curr->next = tmp->next;
            delete tmp;
        }
    }

    void replace(int index, int val) {     // O(index)
        ListNode* curr = head;
        while (index > 0 && curr) {
            curr = curr->next;
            index--;
        }
        if (curr) curr->val = val;
    }

    int peek() {     // O(1)
        return head ? head->val : -1;
    }

    int get(int index) {     // O(index)
        ListNode* curr = head;
        while (index > 0 && curr != nullptr) {
            curr = curr->next;   
            index--;   
        }
        return curr ? curr->val : -1;
    }

    void show() {     // O(n)
        ListNode* curr = head;
        while (curr) {
            std::cout << curr->val;
            if (curr->next) std::cout << " -> ";
            curr = curr->next;
        }
        std::cout << std::endl;
    }

    bool contains(int val) {     // O(n)
        ListNode* curr = head;
        while (curr) {
            if (curr->val == val) return true;
            curr = curr->next;
        }
        return false;
    }

    bool isEmpty() {     // O(1)
        return head == nullptr;
    }

    int size() {     // O(n)
        int length = 0;
        ListNode* curr = head;
        while (curr) {
            curr = curr->next;
            length++;
        }
        return length;
    }

    void reverse() {     // O(n)
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr) {
            ListNode* nextNode = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextNode;
        }
        head = prev;
    }

    void sort() {     // O(nlogn)
        head = mergeSort(head);
    }
};

// --------------- Tests ---------------

int main() {
    SinglyLinkedList list;

    std::cout << "=== Testing push and show ===" << std::endl;
    list.push(3);
    list.push(2);
    list.push(1);
    list.show();   // 1 -> 2 -> 3

    std::cout << "=== Testing insert ===" << std::endl;
    list.insert(1, 99);
    list.show();   // 1 -> 99 -> 2 -> 3

    std::cout << "=== Testing append ===" << std::endl;
    list.append(4);
    list.append(5);
    list.show();   // 1 -> 99 -> 2 -> 3 -> 4 -> 5

    std::cout << "=== Testing pop ===" << std::endl;
    std::cout << "Popped: " << list.pop() << std::endl;
    list.show();   // 1 -> 99 -> 2 -> 3 -> 4

    std::cout << "=== Testing deleteAt ===" << std::endl;
    list.deleteAt(1);  
    list.show();   // 1 -> 2 -> 3 -> 4

    std::cout << "=== Testing remove ===" << std::endl;
    list.remove(3);
    list.show();   // 1 -> 2 -> 4

    std::cout << "=== Testing replace ===" << std::endl;
    list.replace(1, 42);
    list.show();   // 1 -> 42 -> 4

    std::cout << "=== Testing peek ===" << std::endl;
    std::cout << "Peek: " << list.peek() << std::endl;   // 1

    std::cout << "=== Testing get ===" << std::endl;
    std::cout << "Get index 1: " << list.get(1) << std::endl;  // 42

    std::cout << "=== Testing contains ===" << std::endl;
    std::cout << (list.contains(42) ? "Contains 42" : "Does not contain 42") << std::endl;

    std::cout << "=== Testing isEmpty ===" << std::endl;
    std::cout << (list.isEmpty() ? "List is empty" : "List is not empty") << std::endl;

    std::cout << "=== Testing size ===" << std::endl;
    std::cout << "Size: " << list.size() << std::endl;  // 3

    std::cout << "=== Testing reverse ===" << std::endl;
    list.reverse();
    list.show();   // 4 -> 42 -> 1

    std::cout << "=== Testing sort ===" << std::endl;
    list.sort();
    list.show();   // 1 -> 4 -> 42

    return 0;
}
