# Compresses a string using recursive Run-Length Encoding (RLE).
def recursive_rle_compress(data, level=0):
    """    
    Args:
        data: The input string to compress
        level: The current recursion depth (used internally)
    Returns:
        str: The compressed string
    """
    # Base case: if data is empty or recursion level is too deep
    # Prevent excessive recursion
    if not data or level > 10:  
        return data
    
    compressed = []
    i = 0
    n = len(data)
    
    while i < n:
        current_char = data[i]
        
        # Check if we're at the start of a compressed group
        if current_char == '(':
            # Find the matching closing parenthesis
            group_start = i
            balance = 1
            i += 1
            
            while i < n and balance > 0:
                if data[i] == '(':
                    balance += 1
                elif data[i] == ')':
                    balance -= 1
                i += 1
                
            group_end = i - 1
            group = data[group_start + 1:group_end]
            
            # Recursively compress the group content
            compressed_group = recursive_rle_compress(group, level + 1)
            
            # Count repetitions of the group
            j = group_end + 1
            count = 0
            while j < n and data[j].isdigit():
                count = count * 10 + int(data[j])
                j += 1
            
            count = max(1, count)  # At least 1 repetition
            
            if count > 1:
                compressed.append(f"({compressed_group}){count}")
            else:
                compressed.append(f"({compressed_group})")
                
            i = j
        else:
            # Regular character compression
            count = 1
            while i + 1 < n and data[i + 1] == current_char:
                count += 1
                i += 1
            
            if count > 1:
                compressed.append(f"{current_char}{count}")
            else:
                compressed.append(current_char)
            
            i += 1
    
    result = "".join(compressed)
    
    # If we're at the top level, check if we can compress the result further
    if level == 0:
        new_result = recursive_rle_compress(result, level + 1)
        if len(new_result) < len(result):
            return new_result
    
    return result


# Decompresses a string compressed with recursive RLE.
def recursive_rle_decompress(data):
    """
    Args:
        data: The compressed string        
    Returns:
        str: The decompressed string
    """
    decompressed = []
    i = 0
    n = len(data)
    
    while i < n:
        current_char = data[i]
        
        if current_char == '(':
            # Handle compressed group
            group_start = i
            balance = 1
            i += 1
            
            while i < n and balance > 0:
                if data[i] == '(':
                    balance += 1
                elif data[i] == ')':
                    balance -= 1
                i += 1
                
            group_end = i - 1
            group = data[group_start + 1:group_end]
            
            # Get the repetition count
            count = 0
            while i < n and data[i].isdigit():
                count = count * 10 + int(data[i])
                i += 1
            
            # At least 1 repetition
            count = max(1, count)  
            
            # Recursively decompress the group
            decompressed_group = recursive_rle_decompress(group)
            decompressed.append(decompressed_group * count)
        else:
            # Handle regular character
            if i + 1 < n and data[i + 1].isdigit():
                # Character with count
                char = data[i]
                i += 1
                
                # Extract the full count
                count_str = ""
                while i < n and data[i].isdigit():
                    count_str += data[i]
                    i += 1
                
                count = int(count_str) if count_str else 1
                decompressed.append(char * count)
            else:
                # Single character
                decompressed.append(current_char)
                i += 1
    
    return "".join(decompressed)


# Example usage
if __name__ == "__main__":
    test_cases = [
        ("aaabbb", "a3b3"),
        ("aaabbbaaabbb", "(a3b3)2"),
        ("aaaabbbbaaaaabbbbb", "a4b4a5b5"),
        ("abc", "abc"),
        ("aabbcc", "a2b2c2"),
        # Already compressed
        ("((abc)2)3", "((abc)2)3"),  
        ("", ""),
    ]
    print(" Testing compression: ".center(50,"="))
    for original, expected in test_cases:
        compressed = recursive_rle_compress(original)
        decompressed = recursive_rle_decompress(compressed)
        print(f"Original: {original}")
        print(f"Compressed: {compressed}")
        print(f"Decompressed: {decompressed}")
        print(f"Success: {original == decompressed} (Expected: {compressed == expected})")
        print("=".center(50,"="))