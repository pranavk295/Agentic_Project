from mcp.server.fastmcp import FastMCP

mcp = FastMCP("File server")

@mcp.tool()
def read_file(path: str) -> str:
    '''Reads a file and returns the file contents'''
    with open(path, "r") as f:
        return f.read()
    
@mcp.tool()
def write_file(path: str, content: str) -> str:
    '''Writes content to a file and returns a confirmation message'''
    with open(path, "w") as f:
        f.write(content)
    return f"File written successfully: {path}"


@mcp.tool()
def list_files_recursively(directory: str) -> list:
    '''Lists all files in a directory and its subdirectories'''
    import os
    files = []
    for root, dirs, file_list in os.walk(directory):
        for file in file_list:
            files.append(os.path.join(root, file))
    return files


if __name__ == "__main__":
    mcp.run()

