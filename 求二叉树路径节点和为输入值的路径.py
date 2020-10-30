# Problem Description:
# 输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

# Code:
# 方法一：递归(DFS)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        result = []
        if root == None:
            return result
        self.sums = expectNumber
        self.DFS(root, result, [root.val])
        return result
 
    def DFS(self, root, result, path):
        #print(path)
        if root.left == None and root.right == None and sum(path) == self.sums:
            result.append(path)
        if root.left != None:
            #print(root.left.val)
            self.DFS(root.left, result, path+[root.left.val])
        if root.right != None:
            #print(root.right.val)
            self.DFS(root.right, result, path+[root.right.val])

node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(12)
node4 = TreeNode(4)
node5 = TreeNode(7)
print('   ',node1.val)
node1.left = node2
node1.right = node3
print(' ',node1.left.val,' ',node1.right.val)
node2.left = node4
node2.right = node5
print(node2.left.val,'',node2.right.val)
s = Solution()
result = s.FindPath(node1,22)
print(result) # [[10,5,7],[10,12]]

# Runtime:18ms
# Memory footprint:5644KB
# State:Accept

# 方法二：非递归(stack is all you need)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if root == None:
            return []
        result = []
        stack = []
        stack.append((root, [root.val]))
        while stack:
            node, path = stack.pop()
            print(node.val,path)
            if node.left == None and node.right == None and sum(path) == expectNumber:
                result.append(path)
            if node.right != None:
                stack.append((node.right, path + [node.right.val]))
            if node.left != None:
                stack.append((node.left, path + [node.left.val]))
        return result

node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(12)
node4 = TreeNode(4)
node5 = TreeNode(7)
print('   ',node1.val)
node1.left = node2
node1.right = node3
print(' ',node1.left.val,' ',node1.right.val)
node2.left = node4
node2.right = node5
print(node2.left.val,'',node2.right.val)
s = Solution()
result = s.FindPath(node1,22)
print(result) # [[10,5,7],[10,12]]

# Runtime:18ms
# Memory footprint:5624KB
# State:Accept