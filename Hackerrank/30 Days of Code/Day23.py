class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
            return root

    def levelOrder(self, root):
        visit = []

        if root == None:
            return -1
        else:
            q = [root]
            while q:
                visit.append(q[0].data)
                node = q.pop(0)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            print(' '.join(map(str, visit)))


if __name__ == '__main__':
    T = int(input())
    myTree = Solution()
    root = None
    for i in range(T):
        data = int(input())
        root = myTree.insert(root, data)
    myTree.levelOrder(root)