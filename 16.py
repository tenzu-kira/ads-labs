class Node:
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None

def parse_tree(s):
    if not s:
        return None
    def build_tree(start):
        if start >= len(s) or s[start] in ',)':
            return None, start
        value = ''
        while start < len(s) and s[start].isdigit():
            value += s[start]
            start += 1
        node = Node(int(value))
        if start < len(s) and s[start] == '(':
            node.left, start = build_tree(start + 1)
            if start < len(s) and s[start] == ',':
                node.right, start = build_tree(start + 1)
            if start < len(s) and s[start] == ')':
                start += 1
        return node, start
    root, _ = build_tree(0)
    return root

def preorder_non_recursive(root):
    if not root:
        return ""
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(str(node.value))
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return " ".join(result)

tree_str = "8(3(1,6(4,7)),10(,14(13,)))"
root = parse_tree(tree_str)

print("Нерекурсивный прямой обход:")
result = preorder_non_recursive(root)
print(result)
