class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the input path by '/' to get each component of the path
        components = path.split('/')
        
        # Use a stack to keep track of valid directory names
        stack = []
        
        # Iterate over each component in the path
        for part in components:
            if part == '' or part == '.':
                # Ignore empty components and current directory references ('.')
                continue
            elif part == '..':
                # '..' means going up one level, so pop the last directory if the stack is not empty
                if stack:
                    stack.pop()
            else:
                # Add the valid directory or file name to the stack
                stack.append(part)
        
        # Join all elements in the stack with '/' to form the simplified canonical path
        canonical_path = '/' + '/'.join(stack)
        
        return canonical_path

# Create an instance of the Solution class
sol = Solution()

# Example 1
print("=".center(50,"="))
path1 = "/home"
print("Example 1:")
print("Input:", path1)
print("Output:", sol.simplifyPath(path1))
print("=".center(50,"="))

# Example 2
path2 = "/home//foo/"
print("Example 2:")
print("Input:", path2)
print("Output:", sol.simplifyPath(path2))
print("=".center(50,"="))

# Example 3
path3 = "/home/user/Documents/../Pictures"
print("Example 3:")
print("Input:", path3)
print("Output:", sol.simplifyPath(path3))
print("=".center(50,"="))

# Example 4
path4 = "/../"
print("Example 4:")
print("Input:", path4)
print("Output:", sol.simplifyPath(path4))
print("=".center(50,"="))

# Example 5
path5 = "/.../a/../b/c/../d/./"
print("Example 5:")
print("Input:", path5)
print("Output:", sol.simplifyPath(path5))
print("=".center(50,"="))