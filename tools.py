from langchain.tools import tool

@tool
def read_file(path: str) -> str:
    '''Reads a file and returns the file contents'''
    with open(path, "r") as f:
        return f.read()

@tool
def list_files() -> str:
    '''List files in present working directory'''
    import os
    return "\n".join(os.listdir("."))

tools = [read_file,list_files]
