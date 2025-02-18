class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split path by "/" and filter out empty strings
        components = [dir for dir in path.split("/") if dir]
        stack = []
        
        # Process each component
        for comp in components:
            if comp == ".":
                # Current directory - ignore
                continue
            elif comp == "..":
                # Parent directory - pop if stack isn't empty
                if stack:
                    stack.pop()
            else:
                # Regular directory - add to stack
                stack.append(comp)
        
        # Construct the final path
        return "/" + "/".join(stack)