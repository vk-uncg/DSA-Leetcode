# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        q = collections.deque()
        q.append(root)

        

        while(q):
            current_level=[]
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if node:
                    current_level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if current_level:
                result.append(current_level)

        return result



