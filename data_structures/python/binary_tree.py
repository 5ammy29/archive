from collections import deque
from typing import Optional, Any

class TreeNode:
    
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    
    def __init__(self) -> None:
        self.root = None

    def insert(self, val: int) -> None:
        def _insert(node: Optional[TreeNode], val: int) -> TreeNode:
            if node is None:
                return TreeNode(val) 
            elif val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, val)

    def get_depth(self) -> int:
        def _depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_depth = _depth(node.left)
            right_depth = _depth(node.right)
            return 1 + max(left_depth, right_depth)
        return _depth(self.root)

    def contains(self, val: Any) -> bool:
        def _contains(node: Optional[TreeNode], val: Any) -> bool:
            if node is None:
                return False
            elif val == node.val:
                return True
            elif val < node.val:
                return _contains(node.left, val)
            else:
                return _contains(node.right, val)
        return _contains(self.root, val)

    def inorder_traversal(self) -> list[Any]:
        def _inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return None
            # if node is None:
            #     order.append('*') 
            #     return None
            _inorder(node.left)
            order.append(node.val)
            _inorder(node.right)
        order = []
        if self.root is None:
            return []
        _inorder(self.root)
        return order

    def preorder_traversal(self) -> list[Any]:     # Depth-first Search
        def _preorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return None
            # if node is None:
            #     result.append('*') 
            #     return None
            result.append(node.val)    
            _preorder(node.left)             
            _preorder(node.right)            
        if self.root is None:
            return []
        result = []
        _preorder(self.root)
        return result

    def postorder_traversal(self) -> list[Any]:
        def _postorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return None
            # if node is None:
            #     result.append('*') 
            #     return None
            _postorder(node.left)
            _postorder(node.right)
            result.append(node.val)
        if self.root is None:
            return []
        result = []
        _postorder(self.root)
        return result

    def level_order_traversal(self) -> list[Any]:     # Breadth-first Search
        if self.root is None:
            return []
        queue = deque([self.root]) 
        result = []
        while queue:
            node = queue.popleft()  
            result.append(node.val)
            # if node is None:
            #     result.append('*')
            #     continue
            if node.left:
                queue.append(node.left)
            # else:
            #     queue.append(None)
            if node.right:
                queue.append(node.right)
            # else:
            #     queue.append(None)
        return result

    def reverse_inorder_traversal(self) -> list[Any]:
        def _reverse_inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            # if node is None:
            #     order.append('*')
            #     return
            _reverse_inorder(node.right)
            order.append(node.val)
            _reverse_inorder(node.left)
        order = []
        if self.root is None:
            return []
        _reverse_inorder(self.root)
        return order

    def reverse_level_order_traversal(self) -> list[Any]:
        if self.root is None:
            return []
        queue = deque([self.root])  
        stack = []
        while queue:
            node = queue.popleft()
            stack.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return stack[::-1]  

# --------------- Example ---------------

#                    A                    
#                  /   \
#                 B     C
#                / \   / \
#               D   E F   G
# Inorder: ['D', 'B', 'E', 'A', 'F', 'C', 'G']
# Preorder: ['A', 'B', 'D', 'E', 'C', 'F', 'G']
# Postorder: ['D', 'E', 'B', 'F', 'G', 'C', 'A']
# Level Order: ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# Reverse Inorder: ['G', 'C', 'F', 'A', 'E', 'B', 'D']
# Reverse Level Order: ['D', 'E', 'F', 'G', 'B', 'C', 'A']

# --------------- Test ---------------

def test_function():
    bt = BinaryTree()
    assert bt.get_depth() == 0
    for val in [10, 5, 15, 3, 7, 12, 18]:
        bt.insert(val)
    assert bt.inorder_traversal() == [3, 5, 7, 10, 12, 15, 18]
    assert bt.preorder_traversal() == [10, 5, 3, 7, 15, 12, 18]
    assert bt.postorder_traversal() == [3, 7, 5, 12, 18, 15, 10]
    assert bt.level_order_traversal() == [10, 5, 15, 3, 7, 12, 18]
    assert bt.reverse_inorder_traversal() == [18, 15, 12, 10, 7, 5, 3]
    assert bt.reverse_level_order_traversal() == [3, 7, 12, 18, 5, 15, 10]
    assert bt.get_depth() == 3