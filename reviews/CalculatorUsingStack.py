def infix_to_postfix(infix: str):
    precedence_dict = {}
    precedence_dict['('] = 1
    precedence_dict['+'] = 2
    precedence_dict['-'] = 2
    precedence_dict['*'] = 3
    precedence_dict['/'] = 3
    precedence_dict['^'] = 4

    infix_list = infix.split()
    operator_stack = []
    postfix_list = []

    for item in infix_list:
        if item == '(':
            operator_stack.append(item)
        elif item in precedence_dict:
            while operator_stack != [] and precedence_dict[operator_stack[-1]] >= precedence_dict[item]:
                postfix_list.append(operator_stack.pop())
            operator_stack.append(item)
        elif item == ')':
            item = operator_stack.pop()
            while item != '(':
                postfix_list.append(item)
                item = operator_stack.pop()
        else:
            postfix_list.append(item)

    while operator_stack != []:
        postfix_list.append(operator_stack.pop())

    postfix = ' '.join(postfix_list)

    return postfix


def evaluate(postfix):
    operand_stack = []

    postfix_list = postfix.split()

    for item in postfix_list:
        if item in '+-*/^':
            op2 = operand_stack.pop()
            op1 = operand_stack.pop()
            operand_stack.append(do_math(item, op1, op2))
        else:
            operand_stack.append(int(item))

    return operand_stack.pop()


def do_math(op, op1, op2):
    if op == '*':
        res = op1 * op2
    elif op == '/':
        res = op1 / op2
    elif op == '+':
        res = op1 + op2
    elif op == '-':
        res = op1 - op2
    elif op == '^':
        res = op1 ** op2
    return res

def calculate(infix):
    return evaluate(infix_to_postfix(infix))

print(calculate("5 * 3 ^ ( 4 - 2 )"))
