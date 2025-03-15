def paired_parentheses(string):
    stack = []

    for char in string:
        if char == ")":
            if len(stack) == 0:
                return False
            stack.pop()  
        elif char == "(":
            stack.append(char)

    return len(stack) == 0