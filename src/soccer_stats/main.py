"""Main module for the project"""
from typing import Optional
import requests

def hello(name: Optional[str] = None) -> str:
  """Return a greeting message

  Args:
      name (Optional[str], optional): Name to greet. Defaults to None.

  Returns:
      str: A greeting message
  """
  if name is None:
    return "Hello World!"
  return f"Hello, {name}!"

  
if __name__ == "__main__":
  print(hello())
  url = "https://jsonmock.hackerrank.com/api/football_teams"
  res = requests.get(url)
  data = res.json()
  print(data)
