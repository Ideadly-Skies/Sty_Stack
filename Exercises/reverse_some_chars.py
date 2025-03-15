def reverse_some_chars(s, chars):
    chars_dict = { c:0 for c in chars }
    stack = []

    for char in s:
        # O(1) (reduced from O(n))
        if char in chars_dict:
            stack.append(char)

    # construct output str
    output = ""
    for char in s:
        if char in chars_dict:
            output += stack.pop()
        else:
            output += char 

    return output

if __name__ == "__main__":
    print(reverse_some_chars("computer", ["a", "e", "i", "u", "o"]))