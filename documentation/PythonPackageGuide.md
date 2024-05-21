# How to Python Packages

I had some troubles with python packages, which led to messy imports. 
This guide helps navigate the use of python packages. This guide assumes basic python knowledge

## Initialising a package
Any directory with a `__init__.py` becomes a python package. You can then use this package in other parts of the code.
Example:
```
Any_Folder > Python package!
|- __init__.py
|- tools.py
|- ...
```
## Putting things into a package
In the `__init__.py` file, import things you want from other files within the directory.
E.g. in `tools.py`,
```python
def multiply(a: int, b: int) -> int:
    return a * b
```
Then in `__init__.py`
```python
from Any_Folder.tools import multiply
```
Then you can import `multiply` directly from the `Any_Folder` package!