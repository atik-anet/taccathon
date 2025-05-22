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
mcp = FastMCP("Demo")

@mcp.tool()
async def get_tree_folders(directory: str) -> str:
    """
    Get the directory tree structure of a given directory.
    
    Args:
        directory: The directory path to explore.
    
    Returns:
        The text output of the 'tree' command representing the directory structure.
    """
    url = f"http://{ip}:{port}/tree?directory=SandTunnel"

    try:
        response = requests.get(url)  # or requests.post(url, json=payload) if it requires POST
        response.raise_for_status()  # Raises HTTPError if the response was an error
        data = response.json()  # or response.text if the response isn't JSON
        return data
    except requests.exceptions.RequestException as e:
       print(e)
       print(url)
       return {"exception":"couldnot find"}

@mcp.tool()
async def get_weather(city: str) -> str:
    """
     Get the weather information for a specified city.

     Args:
         city (str): The name of the city to get weather information for.

     Returns:
         str: A message containing the weather information for the specified city.
     """
    return f"The weather in {city} is sunny."


app.mount("/", mcp.sse_app())