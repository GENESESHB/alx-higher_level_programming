# 0x0B-python-input_output


# Here's a concise version of the function that reads a text file and prints its contents to stdout:

```python
def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
```

This function uses the `with` statement to open the file, reads its contents using `file.read()`, and then prints the content to stdout without adding an extra newline character.

You can call this function with the desired filename to read and print the contents of the file.

Let me know if you have any further questions!
