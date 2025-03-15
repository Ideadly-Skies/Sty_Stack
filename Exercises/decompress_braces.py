def decompress_braces(string):
    stack = [] 
    
    for char in string:
        if char == "}":
            # variable to store sub_seq
            segment = "" 
            
            # create sub_seq (reversed)
            while not stack[-1].isnumeric():
                popped = stack.pop()
                segment = popped + segment

            # pop the number and concatenate sub_seq 
            stack.append(segment * int(stack.pop()))
        
        elif char != "{":
            stack.append(char)            

    # reconstruct string from front
    return ''.join(stack)

if __name__ == "__main__":
    print(decompress_braces("z3{a2{xy}b}"))
    # -> zaxyxybaxyxybaxyxyb