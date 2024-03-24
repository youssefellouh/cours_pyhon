def DashInsertII(s):
    result = ''
    
    for i in range(len(s) - 1):
        current_digit = int(s[i])
        next_digit = int(s[i + 1])
        
        result += str(current_digit)
        
        if current_digit % 2 == 0 and next_digit % 2 == 0 and current_digit != 0 and next_digit != 0:
            result += ' x '
        elif current_digit % 2 != 0 and next_digit % 2 != 0 and current_digit != 0 and next_digit != 0:
            result += ' - '
    
    # Add the last digit
    result += s[-1]
    
    return result

# Example usage:
#input_str = "4546793"
#output_str = dash_insert_ii(input_str)
print(DashInsertII("4546793"))
print(DashInsertII("99946"))
print(DashInsertII("56647304"))