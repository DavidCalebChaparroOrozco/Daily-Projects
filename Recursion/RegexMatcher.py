# Matches a single character against a pattern character.
# Supports '.' as wildcard and character groups like [abc].
def match_char(char, pattern):
    if not pattern:
        return False

    # Wildcard support: '.' matches any character
    if pattern[0] == '.':
        return True

    # Character group support: [abc]
    if pattern[0] == '[':
        closing = pattern.find(']')
        if closing == -1:
            raise ValueError("Unclosed character group")
        group = pattern[1:closing]
        return char in group

    return char == pattern[0]


# Recursively matches the string `s` against the pattern `pattern`.
# Supports '.', '*', '+', '?', and '[abc]' syntax.
def match_pattern(s, pattern):
    # Base case: if pattern is empty, s must also be empty
    if not pattern:
        return not s

    # Handle group [abc] as a single token
    if pattern[0] == '[':
        closing = pattern.find(']')
        if closing == -1:
            raise ValueError("Unclosed character group")
        token = pattern[:closing + 1]
        rest = pattern[closing + 1:]
    else:
        token = pattern[0]
        rest = pattern[1:]

    # Check for quantifiers: '*', '+', '?'
    if rest and rest[0] in '*+?':
        quantifier = rest[0]
        rest = rest[1:]

        if quantifier == '*':
            # Match zero or more of token
            return (match_pattern(s, rest) or
                    (s and match_char(s[0], token) and match_pattern(s[1:], pattern)))
        elif quantifier == '+':
            # Match one or more of token
            return (s and match_char(s[0], token) and
                    (match_pattern(s[1:], rest) or match_pattern(s[1:], pattern)))
        elif quantifier == '?':
            # Match zero or one of token
            return (match_pattern(s, rest) or
                    (s and match_char(s[0], token) and match_pattern(s[1:], rest)))
    else:
        # No quantifier: match one occurrence
        return (s and match_char(s[0], token) and match_pattern(s[1:], rest))


test_cases = [
    # . matches any character
    ("abc", "a.c"),          
    # [bd] matches b
    ("abc", "a[bd]c"),       
    # should fail
    ("abc", "a[xyz]c"),      
    # * matches zero or more a
    ("aaaabc", "a*bc"),      
    # + matches one or more a
    ("aabc", "a+bc"),        
    # ? matches zero or one a
    ("bc", "a?bc"),          
    # multiple + usage
    ("abc", "a+b+c+"),       
    # [abc]* matches zero of [abc]
    ("xyz", "x[abc]*z"),     
    # not supported - grouping
    ("xabcabcz", "x([abc]+)+z"), 
]

for string, pattern in test_cases:
    try:
        result = match_pattern(string, pattern)
        print(f"match('{string}', '{pattern}') → {result}")
    except Exception as e:
        print(f"Error matching '{string}' with '{pattern}': {e}")
