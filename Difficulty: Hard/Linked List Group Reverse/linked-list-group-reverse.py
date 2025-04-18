"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        return self._reverse(head, k)
    
    def _reverse(self, head, k):
        prev, node = None, head
        for _ in range(k):
            if node is None:
                return prev
            prev, node.next, node = node, prev, node.next
        if node:
            head.next = self._reverse(node, k)
        return prev

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())  # Number of test cases
    while t > 0:
        llist = LinkedList()

        # Read list values and push them to the LinkedList
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)

        k = int(input())  # Size of the group for reversal
        ob = Solution()
        new_head = ob.reverseKGroup(llist.head, k)
        llist.head = new_head
        llist.printList()  # Print the modified linked list
        t -= 1

        print("~")

# } Driver Code Ends