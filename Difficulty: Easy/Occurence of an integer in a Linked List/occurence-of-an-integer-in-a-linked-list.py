"""  
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def count(self, head, key):
        # Code here
        fast = head
        ans = 0
        
        while fast != None and fast.next != None:
            if fast.data == key:
                ans += 1
            if fast.next.data == key:
                ans += 1
            
            fast = fast.next.next
    
        return ans + (1 if fast != None and fast.data == key else 0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0])
    for i in range(1, t + 1):
        arr = list(map(int, data[2 * i - 1].split()))
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        key = int(data[2 * i])
        ob = Solution()
        print(ob.count(head, key))
        print("~")

# } Driver Code Ends