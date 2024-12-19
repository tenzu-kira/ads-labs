class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        if root.left is None:
            root.left = Node(data)
        else:
            insert(root.left, data)
    elif data > root.data:
        if root.right is None:
            root.right = Node(data)
        else:
            insert(root.right, data)
    return root

def delete(root, key):
    if not root:
        return root
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)
    return root

def minValueNode(node):
    current = node
    while current.left:
        current = current.left
    return current

def search(root, key, path=None):
    if path is None:
        path = []
    if not root or root.data == key:
        if root:
            path.append(root.data)
        return root, path
    path.append(root.data)
    if key < root.data:
        return search(root.left, key, path)
    return search(root.right, key, path)

def print_menu():
    print("\nВыберите операцию:")
    print("1. Добавить вершину")
    print("2. Удалить вершину")
    print("3. Найти вершину")
    print("4. Вывести дерево")
    print("5. Выйти из программы")

def print_tree(root):
    print("\nДерево:")
    print_tree_format(root)

def print_tree_format(root):
    if not root:
        return
    print(root.data, end=" ")
    if root.left or root.right:
        print("(", end=" ")
        print_tree_format(root.left)
        print(", ", end=" ")
        print_tree_format(root.right)
        print(")", end=" ")

def main():
    tree = None

    while True:
        print_menu()
        choice = input("Введите номер операции: ")

        if choice == '1':
            value = int(input("Введите значение для добавления: "))
            tree = insert(tree, value)
            print("Вершина добавлена.")
        elif choice == '2':
            value = int(input("Введите значение для удаления: "))
            tree = delete(tree, value)
            print("Вершина удалена.")
        elif choice == '3':
            value = int(input("Введите значение для поиска: "))
            result, path = search(tree, value)
            if result:
                print(f"Вершина {value} найдена. Путь к вершине: {path}")
            else:
                print(f"Вершина {value} не найдена.")
        elif choice == '4':
            print_tree(tree)
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()