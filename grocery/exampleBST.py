class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

leaf_4, leaf_5, leaf_6, leaf_7 = TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
root = TreeNode(1)
node_2.left, node_2.right = leaf_4, leaf_5
node_3.left, node_3.right = leaf_6, leaf_7
root.left, root.right = node_2, node_3

level = [root]
nextLevel = []
queue = []
while level:
    queue.extend(level)
    print(queue)
    for l in level:
        if l.left != None and l.right != None:
            nextLevel.append(l.left, l.right)
        if l.left != None and l.right == None:
            nextLevel.append(l.left)
        if l.left == None and l.right != None:
            nextLevel.append(l.right)
    level = nextLevel
    nextLevel = []
