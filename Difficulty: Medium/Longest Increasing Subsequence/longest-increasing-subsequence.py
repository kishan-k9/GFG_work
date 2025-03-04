from bisect import bisect_left as search
class Solution:
    def lis(self, arr):
       ans=[]
       for e in arr:
           i = search(ans, e)
           if i < len(ans):
               ans[i] = e
           else:
               ans.append(e)
       return len(ans)


       



#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.lis(a))
        print("~")
# } Driver Code Ends