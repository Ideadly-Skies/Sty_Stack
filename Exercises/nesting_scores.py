def nesting_score(string):
    stack = [0]

    for i in range(len(string)):
        if string[i] == "[":
            stack.append(0)
        elif string[i] == "]":
            popped = stack.pop()

            # if 0 is at the top of the stack
            if popped == 0:
                stack[-1] += 1
            
            # multiply 2 to the top of the stack
            if popped > 0:
                popped *= 2
                stack[-1] += popped
    
    return stack.pop()

if __name__ == "__main__":
    pass