from stack import Stack

def check_balance(brackets: str) -> bool:
    '''The argument brackets is the string of brackets.
    For example, "[[{())}]".
    Output:
    If brackets balanced "{{[()]}}" - True
    otherwise "[[{())}]" - False
    '''
    brackets_stack = Stack()
    for i in range(len(brackets)):
        if brackets_stack.size() == 0:
            brackets_stack.push(brackets[i])
            continue
        if brackets[i] == ")" and brackets_stack.peek() == "(":
            brackets_stack.pop()
            continue
        elif brackets[i] == "]" and brackets_stack.peek() == "[":
            brackets_stack.pop()
            continue
        elif brackets[i] == "}" and brackets_stack.peek() == "{":
            brackets_stack.pop()
            continue
        else:
            brackets_stack.push(brackets[i])
    return brackets_stack.is_empty()


if __name__ == "__main__":
    expression = input("Введите сторку, содержащую только скобки: ")
    balance = check_balance(expression)
    if (balance):
        print("Сбалансированно")
    else:
        print("Несбалансированно")

        

