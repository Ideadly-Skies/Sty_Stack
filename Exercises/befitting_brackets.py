def befitting_brackets(string):
    bracket_dict = {"(": ")", "{": "}", "[": "]"} 
    stack = []

    for char in string:
        if char in bracket_dict:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            
            if bracket_dict[stack[-1]] == char: 
                stack.pop()

    return len(stack) == 0

if __name__ == "__main__":
    print(befitting_brackets('(){}[](())')) # -> True
    print(befitting_brackets('({[]})')) # -> True
    print(befitting_brackets('[][}')) # -> False