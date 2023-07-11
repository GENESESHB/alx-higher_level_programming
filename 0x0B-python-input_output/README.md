# 0x0B-python-input_output


# Here's a concise version of the function that reads a text file and prints its contents to stdout:

```python
def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
```

This function uses the `with` statement to open the file, reads its contents using `file.read()`, and then prints the content to stdout without adding an extra newline character.

You can call this function with the desired filename to read and print the contents of the file.


# Here's a concise version of the function that writes a string to a text file and returns the number of characters written:

```python
def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as file:
          return file.write(text)
```

This function uses the `with` statement to open the file in write mode, writes the content of the `text` parameter to the file using `file.write()`, and returns the number of characters written.

You can call this function with the desired filename and text to write the content to the file and obtain the number of characters written.



# Here is a Python function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

```python
def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
```

If the file doesn’t exist, it will be created. The function uses the with statement to ensure that the file is closed when the block inside the with statement is exited. You don’t need to manage file permission or file doesn't exist exceptions. Also, you are not allowed to import any models


# Here’s a Python function that returns the JSON representation of an object (string):

```python
import json

def to_json_string(my_obj):
    return json.dumps(my_obj)
```

This function uses the built-in JSON library in Python. The json.dumps() method is used to convert a Python object into a JSON string. If the object cannot be serialized


# Here's the implementation of the `from_json_string` function in Python:

```python
import json

def from_json_string(my_str):
    return json.loads(my_str)
```

The `json.loads()` function is used to parse the JSON string and convert it into a Python object. It automatically handles converting the JSON data into appropriate Python data structures such as lists and dictionaries.

You can use this function to parse JSON strings and retrieve the corresponding Python objects. Here's an example usage based on the code snippet you provided:

```python
s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))

s_my_dict = """
{"is_active": true, "info": {"age": 36, "average": 3.14}, 
"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
"""
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))

try:
    s_my_dict = """
    {"is_active": true, 12 }
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

This will output:

```
[1, 2, 3]
<class 'list'>
{'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': ['San Francisco', 'Tokyo']}
<class 'dict'>
[ValueError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
```

Note that the `json.loads()` function may raise a `ValueError` if the JSON string is not properly formatted. You can handle this exception to manage cases where the JSON string doesn't represent an object, as mentioned in the prompt.
