#User function Template for python3
class Solution:
    def largestBst(self, root):
        # Your code here
        def walk(n):
            if not n:
                return True, 0, float('inf'), float('-inf')
            lf, lsize, lmin, lmax = walk(n.left)
            rf, rsize, rmin, rmax = walk(n.right)
            
            if lf and rf and lmax < n.data < rmin:
                return True, 1+lsize+rsize, min(n.data, lmin), max(n.data, rmax)
            
            return False, max(lsize, rsize), 0, 0
        
        _, r, _, _ = walk(root)
        return r

#{ 
 # Driver Code Starts
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input string after splitting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size += 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q.popleft()
        size -= 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)
            size += 1

        # Move to the next element
        i += 1
        if i >= len(ip):
            break

        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.right)
            size += 1

        # Move to the next element
        i += 1

    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        result = ob.largestBst(root)
        print(result)

# } Driver Code Ends