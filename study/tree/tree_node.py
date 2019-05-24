from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        queue = [self]
        res = defaultdict(list)
        level = 0
        while queue:
            node = queue.pop(0)
            res[level].append(node)
            if len(res[level]) >= 2 ** level:
                if not any(res[level]):
                    level -= 1
                    break
                level += 1
            if not node:
                queue.append(None)
                queue.append(None)
            else:
                queue.append(node.left)
                queue.append(node.right)
        for i in range(level + 1):
            s = ','.join(str(node.val).center(4, '-') if node else 'None' for node in res[i])
            print(s.center(2 ** level * 5))
            print()
        return ''

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return str(self) == str(other)

    @staticmethod
    def create_tree(list):
        if not list:
            return None
        root = TreeNode(list[0])
        queue = [root]
        node = None
        for i, val in enumerate(list[1:]):
            if i % 2 == 0:
                node = queue.pop(0)
                if val is not None:
                    node.left = TreeNode(val)
                    queue.append(node.left)
            else:
                if val is not None:
                    node.right = TreeNode(val)
                    queue.append(node.right)
        return root
