import operator

from BinaryTree import BinaryTree


def parse_tree(formula):
    tokens = formula.split()
    stack = []
    tree = BinaryTree('')
    currentnode = tree
    stack.append(tree)
    for token in tokens:
        if token == '(':
            currentnode.insert_left('')
            stack.append(currentnode)
            currentnode = currentnode.get_left_child()
        elif token == ')':
            currentnode = stack.pop()
        elif token not in ['+', '-', '*', '/', 'and', 'or', 'not']:
            currentnode.set_root_val(int(token))
            currentnode = stack.pop()
        elif token in ['+', '-', '*', '/', 'and', 'or']:
            currentnode.set_root_val(token)
            stack.append(currentnode)
            currentnode.insert_right('')
            currentnode = currentnode.get_right_child()
        elif token == 'not':
            currentnode = stack.pop()
            currentnode.set_root_val(token)
            stack.append(currentnode)
            currentnode.insert_right('')
            currentnode = currentnode.get_right_child()
        else:
            raise ValueError(token)

    return tree


operator_dict = {'+': operator.add, '-': operator.sub,
                 '*': operator.mul, '/': operator.truediv,
                 'not': operator.not_, 'and': operator.and_,
                 'or': operator.or_}


def evaluate_tree(tree: BinaryTree):
    token = tree.get_root_val()
    left_tree = tree.get_left_child()
    right_tree = tree.get_right_child()

    if token == 'not':
        opt = operator_dict.get(token, None)
        return opt(evaluate_tree(right_tree))
    elif token in ['+', '-', '*', '/', 'and', 'or']:
        opt = operator_dict.get(token, None)
        return opt(evaluate_tree(left_tree), evaluate_tree(right_tree))
    else:
        return token


def inorder_traversal(tree: BinaryTree):
    expression = ""
    if tree:
        leftchild = tree.get_left_child()
        if leftchild:
            expression += '( ' + inorder_traversal(leftchild)

        if str(tree.get_root_val()):
            expression += str(tree.get_root_val()) + ' '

        rightchild = tree.get_right_child()
        if rightchild:
            expression += inorder_traversal(tree.get_right_child()) + ') '

    return expression


pt = parse_tree("( ( 3 + 4 ) and ( not 0 ) )")
print(evaluate_tree(pt))
print(inorder_traversal(pt))
