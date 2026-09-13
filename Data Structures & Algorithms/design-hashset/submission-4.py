class ListNode:
    def __init__(self, key):
        self.key = key
        self.next_node = None

class MyHashSet:

    def __init__(self):
        self.hashset = [ListNode(-1) for i in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.hashset)
        curr_node = self.hashset[index]
        while (curr_node.next_node != None):
            if curr_node.key == key:
                return
            curr_node = curr_node.next_node
        if curr_node.key == key:
            return
        curr_node.next_node = ListNode(key)
        return

    def remove(self, key: int) -> None:
        index = key % len(self.hashset)
        prev = None
        curr = self.hashset[index]
        while (curr != None and curr.key != key):
            prev = curr
            curr = curr.next_node
        if curr != None:
            prev.next_node = curr.next_node
            curr.next_node = None
        return

    def contains(self, key: int) -> bool:
        index = key % len(self.hashset)
        curr = self.hashset[index]
        while (curr != None):
            if curr.key == key:
                return True
            curr = curr.next_node
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)