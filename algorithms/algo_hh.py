def isWordPresentInMatrix(matrix, word):
    row = len(matrix)
    cols = len(matrix[0])

    def nextt(r, c, index):
        if index == len(word):
            return True
        if (r < 0 or r >= row or c < 0 or c >= cols or matrix[r][c] != word[index]):
            return False
        
        z = matrix[r][c]
        matrix[r][c] = '----'
        f = (nextt(r + 1, c, index + 1) or nextt(r - 1, c, index + 1) or nextt(r, c + 1, index + 1) or nextt(r, c - 1, index + 1))
        matrix[r][c] = z
        return f

    for r in range(row):
        for c in range(cols):
            if matrix[r][c] == word[0] and nextt(r, c, 0):
                return True
    return False


#тестирование

matrix = [
    ['A', 'F', 'H', 'D', 'H'],
    ['O', 'O', 'E', 'P', 'E'],
    ['L', 'L', 'L', 'L', 'L']
]

word = 'HELLO'
print(isWordPresentInMatrix(matrix, word))


# -----------------------------

# Дано бинарное дерево. Найдите наименьшего общего предка (LCA) для двух заданных значений в дереве.


#         1
#        / \
#       2   3
#      / \   \
#     4  5    6
    

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def lca(node: Node, val1:int, val2:int) -> int | Node | None:
    if node is None:
        return None
        
    if node.value == val1 or node.value == val2:
        return node

    left = lca(node.left, val1, val2)
    right = lca(node.right, val1, val2)
    if left and right:
        return node
    elif left:
        return left
    else:
        return right


