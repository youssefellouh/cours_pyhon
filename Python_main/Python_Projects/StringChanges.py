def StringChanges(str):
    result = ''
    prev_char = ''

    for char in str:
        if char == 'M':
            result += prev_char
        elif char == 'N':
            # Skip the next character
            pass
        else:
            result += char
            prev_char = char

    return result

# Example usage:
input_str = "abcNdgM"
output_str = StringChanges(input_str)
print(output_str)
print(StringChanges("abcNdgM"))
