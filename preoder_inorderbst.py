# Time complexity : O(n) - Linear time
# Space complexity : O(H) //H is height of the Binary Tree
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
          
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
       
        root.left = self.buildTree(preorder[1:root_index + 1],inorder[:root_index])
        
        root.right = self.buildTree(preorder[root_index + 1: ],inorder[root_index + 1:])
        
        return root