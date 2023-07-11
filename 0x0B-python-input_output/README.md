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

Let me know if there's anything else I can help you with!
