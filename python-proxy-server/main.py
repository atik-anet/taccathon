import os
import subprocess
from typing import Any
from PmtBatt.Utils.PackageSearcher import PackageSearcher
from opengrokclient import grok
import pdb
from fastapi import FastAPI

app = FastAPI()

# code.
@app.get("/read/")
def read_file(file_path: str ):
   """
   Reads the content of a file using helper API( GetFileContent ).

   Args:
      file_path: Absolute or relative file path.
    
   Returns:
      The file content or an error message.
   """
   file_path = file_path.split('/')
   project = file_path[1]
   package = file_path[3]
   final_file_path = '/'.join(file_path[4:])
   ps = PackageSearcher(project,package)
   return ps.GetFileContent( final_file_path )

# symbol defination
@app.get("/search/definition/")
async def get_symbol_definiton(symbolName:str ):
   """
   Returns list of files contain function/class defination.

   Args:
      symbolName: Name of the function/class.

   Returns:
      jsonResponse (dict): JSON response, or None if there was an error. 
   """
   try:
      #  parse response to give only filename, linenumber
      result= grok.doGrokRequest( definition=symbolName )
      return result
   except Exception as e:
        return f"Error symbol definition: {str(e)}"

# symbol search in path
@app.get("/search/symbol/")
def searchSymbolInPath(path:str, symbol: str ):
   """
   Search symbol in the given directory/file path.
    
   Args:
      path: The directory/file path to explore.
      symbol: symbol to search in the provided path argument.
    
   Returns:
      A list of all the filenames in the given path matching the symbol,if provided. 
   """
   path = path.split('/')
   project = path[1]
   package = path[3]
   final_path = '/'.join(path[4:])
   ps = PackageSearcher(project,package)
   return ps.GetFileNamesInPath( final_path, symbol )

@app.get("/tree")
def get_tree_folders(directory: str):
    """
    Returns the directory tree structure using the 'tree' command.
    
    Args:
        directory: The directory path to explore.
    
    Returns:
        The text output of the 'tree' command representing the directory structure.
    """
    if not os.path.isdir(f"/src/{directory}"):
        return f"Error: '{directory}' is not a valid directory."
    try:
        result = subprocess.run(
            ["tree", "/src/"+directory],
            capture_output=True,
            text=True,
            check=True
        )
        return {"result":result.stdout}
    except Exception as e:
        return f"Error generating directory tree: {str(e)}"

@app.get("/test")
async def root():
    return {"message": "Hello World from old python container"}