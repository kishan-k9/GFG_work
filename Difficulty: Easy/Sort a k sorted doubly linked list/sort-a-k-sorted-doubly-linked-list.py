#User function Template for python3
'''
class DLLNode:
    def __init__(self,val) -> None:
        self.data = val
        self.prev = None
        self.next = None
'''
class Solution:
    def sortAKSortedDLL(self, head, k):
        # Code Here
        from heapq import heappush, heappop
        
        p = q = head
        h = []
        while q:
            heappush(h, q.data)
            if len(h) >= k+1:
                p.data = heappop(h)
                p = p.next
            q = q.next
        while h:
            p.data = heappop(h)
            p = p.next
        return head

#{ 
 # Driver Code Starts
import heapq


# A node of the doubly linked list
class DLLNode:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


# Function to insert a node at the end of the doubly linked list
def push(tail, new_data):
    new_node = DLLNode(new_data)
    new_node.next = None
    new_node.prev = tail

    if tail is not None:
        tail.next = new_node

    return new_node


# Function to print nodes in a given doubly linked list
def printList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


# Driver code
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    for _ in range(t):
        arr = list(map(int, input().split()))  # Read the input array
        k = int(input())  # Read the value of k

        head = DLLNode(arr[0])
        tail = head

        for i in range(1, len(arr)):
            tail = push(tail, arr[i])

        solution = Solution()
        sorted_head = solution.sortAKSortedDLL(head, k)
        printList(sorted_head)

# } Driver Code Ends