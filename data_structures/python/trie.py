class TrieNode:

    def __init__(self, val: str = '') -> None:
        self.val = val
        self.children = {}  
        self.is_leaf = False  

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:     # O(len(word))
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.is_leaf = True

    def search(self, word: str) -> bool:     # O(len(word))
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_leaf

    def starts_with(self, prefix: str) -> bool:     # O(len(prefix))
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word: str) -> None:     # O(len(word))
        def _delete(node: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                if not node.is_leaf:
                    return False  
                node.is_leaf = False
                return len(node.children) == 0  
            char = word[index]
            child = node.children.get(char)
            if not child:
                return False  
            should_delete_child = _delete(child, word, index + 1)
            if should_delete_child:
                del node.children[char]  
                return not node.is_leaf and len(node.children) == 0
            return False
        _delete(self.root, word, 0)

# --------------- Tests ---------------

def test_insert_and_search():
    trie = Trie()
    trie.insert("car")
    trie.insert("cat")
    trie.insert("dog")
    assert trie.search("car") == True
    assert trie.search("cat") == True
    assert trie.search("dog") == True
    assert trie.search("cow") == False
    assert trie.search("ca") == False  

def test_starts_with():  
    trie = Trie()
    trie.insert("car")
    trie.insert("cat")
    trie.insert("dog")
    assert trie.starts_with("ca") == True
    assert trie.starts_with("do") == True
    assert trie.starts_with("cu") == False

def test_delete():
    trie = Trie()
    trie.insert("car")
    trie.insert("cat")
    trie.insert("dog")
    trie.delete("cat")
    assert trie.search("cat") == False
    assert trie.search("car") == True  
    assert trie.search("dog") == True
    trie.delete("cow") 
    assert trie.search("cow") == False