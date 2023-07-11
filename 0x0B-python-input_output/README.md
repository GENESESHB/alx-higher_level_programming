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

Note that the `json.loads()` function may raise a `ValueError` if the JSON string is not properly formatted. You can handle this exception to manage cases where the JSON string doesn't represent an object,


#  Here's the implementation of the `save_to_json_file` function in Python:

```python
import json

def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
```

The `save_to_json_file` function takes two parameters: `my_obj`, which is the object to be saved to the file, and `filename`, which is the name of the file to save the object to.

Within the function, the `open()` function is used to open the file in write mode. The `json.dump()` function is then used to serialize the object (`my_obj`) and write it to the file in JSON format.

The function utilizes the `with` statement, which ensures that the file is automatically closed after the operation, even if an exception occurs.

Here's an example usage of the function based on the code snippet you provided:

```python
filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

This code will save the `my_list` object to the file "my_list.json", the `my_dict` object to the file "my_dict.json", and attempt to save the `my_set` object to the file "my_set.json". However, since sets are not JSON serializable, it will raise a `TypeError` exception.

The resulting files will contain the JSON representation of the respective objects:

Contents of "my_list.json":
```
[1, 2, 3]
```

Contents of "my_dict.json":
```
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
```

Note that the code doesn't handle exceptions for cases where the object cannot be serialized or file permission exceptions.



# Here's the implementation of the `load_from_json_file` function that creates an object from a JSON file:

```python
import json

def load_from_json_file(filename):
    with open(filename, 'r') as file:
        json_data = file.read()
        obj = json.loads(json_data)
        return obj
```

This function takes a `filename` as input and reads the contents of the file using the `open` function within a `with` statement. It then reads the file data using `file.read()` and uses `json.loads()` to parse the JSON data and convert it into a Python object. Finally, it returns the created object.

Note that exceptions related to file permissions or file not found are not managed in this implementation, as specified in the requirements.

You can use this function as shown in the example you provided:

```python
filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

This code will load the JSON data from the specified files and print the loaded objects along with their types. It also handles exceptions if the file doesn't exist or if the JSON string doesn't represent a valid object.


#  Here's an example of how you can use the `class_to_json` function from the provided solution, along with a sample class, and the corresponding input and output.

`my_class.py`:
```python
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"MyClass(name={self.name}, age={self.age})"
```

`main.py`:
```python
from my_class import MyClass
from class_to_json import class_to_json

# Create an instance of MyClass
obj = MyClass("John", 25)

# Serialize the object to JSON representation
json_data = class_to_json(obj)

# Print the output
print(json_data)
```

Output:
```
{'name': 'John', 'age': 25}
```

Explanation:
In this example, we have a class `MyClass` defined in `my_class.py`. The class has two attributes, `name` and `age`, along with an overridden `__str__` method.

In `main.py`, we import the `MyClass` and `class_to_json` functions. We create an instance of `MyClass` with the name "John" and age 25.

Next, we call the `class_to_json` function with the `obj` instance as an argument, which returns the JSON-compatible dictionary representation of the object.

Finally, we print the `json_data` dictionary, which represents the serialized object in JSON format.

The output shows the resulting dictionary with the attributes `'name'` and `'age'` and their corresponding values, `'John'` and `25`, respectively.
