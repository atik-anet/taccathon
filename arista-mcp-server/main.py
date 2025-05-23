# server.py
from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI
import requests

app = FastAPI()
ip = "10.224.23.44"
port = "8000"

@app.get("/test")
async def root():
    return {"message": "Hello World"}

# Create an MCP server
mcp = FastMCP("AristaCodeAssist")

@mcp.tool()
async def get_tree_folders(path: str):
    """
    Get the directory tree structure of a given directory path.
    
    Args:
        path: The directory path to explore.
    
    Returns:
        The json output of the 'tree' command representing the directory structure.
    """
    url = f"http://{ip}:{port}/tree?directory={path}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
       print(e)
       print(url)
       return {"exception":"couldnot find"}

@mcp.tool()
def read_file(file_path: str ):
    """
    Reads the content of a file using get request.

    Args:
        file_path: Absolute or relative file path.
        
    Returns:
        The file content in json format or an error message.
    """
    url = f"http://{ip}:{port}/read?file_path={file_path}"
    try:
        response = requests.get(url) 
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
       print(e)
       print(url)
       return {"exception":"couldnot find"}
   
@mcp.tool()
async def get_symbol_definiton(symbolName:str ):
    """
    Reads the list of files contains symbol(function/class) defination 
        using get request.

    Args:
        symbolName: Name of the function/class.

    Returns:
        jsonResponse (dict): JSON response, or None if there was an error. 
    """
    url = f"http://{ip}:{port}/search/definition?symbolName={symbolName}"
    try:
        response = requests.get(url) 
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
       print(e)
       print(url)
       return {"exception":"couldnot find"}

@mcp.tool()
def searchSymbolInPath(path:str, symbol: str ):
    """
    Search symbol(function/class/attribute) in the given directory/file path.
    
    Args:
        path: The directory/file path to explore.
        symbol: symbol to search in the provided path argument.
    
    Returns:
        A list of all the filenames in the given path matching the symbol in json 
        format. 
    """
    url = f"http://{ip}:{port}/search/symbol?path={path}&symbol={symbol}"
    try:
        response = requests.get(url) 
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
       print(e)
       print(url)
       return {"exception":"couldnot find"}

@mcp.tool()
def learn_tacc_concepts():
    """
    Learn tacc conceptsI
    
    Args:
        No Args
    
    Returns:
        A text which explains basic tacc syntax
    """
    url = f"http://{ip}:{port}/learn"
    try:
        response = requests.get(url) 
        response.raise_for_status() 
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
       print(e)
       print(url)
       return {"exception":"couldnot find"}





app.mount("/", mcp.sse_app())