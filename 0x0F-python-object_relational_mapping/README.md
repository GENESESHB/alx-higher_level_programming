![ORM](https://miro.medium.com/v2/resize:fit:1200/format:png/1*9TZHTGKjIyUOAvmQkV1RNA.png)

# 0x0F-python-object_relational_mapping

# ``Background Context 📑``

[ALL](https://intranet.alxswe.com/projects/283)

# ``Tasks 🚀``

# ``list T from DB ``

Let's break down the code line by line:

```python
#!/usr/bin/python3
```
- This is called a shebang line and specifies the path to the Python interpreter that should be used to execute the script. In this case, it points to the Python 3 interpreter.

```python
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
```
- These are comments that provide a description of the script's purpose and usage. They explain that the script lists all states from a database called `hbtn_0e_0_usa` and how to use it with command-line arguments.

```python
import sys
```
- This line imports the `sys` module, which provides access to command-line arguments and other system-related functions.

```python
import MySQLdb
```
- This line imports the `MySQLdb` module, which is a Python interface for interacting with MySQL databases.

```python
if __name__ == "__main__":
```
- This line checks whether the script is being run directly (as opposed to being imported as a module into another script). Code within this block will only execute if the script is the main entry point.

```python
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
```
- This line establishes a connection to a MySQL database using the `MySQLdb.connect()` method. It uses the command-line arguments provided when running the script:
   - `sys.argv[1]`: The first argument is the MySQL username.
   - `sys.argv[2]`: The second argument is the MySQL password.
   - `sys.argv[3]`: The third argument is the name of the database.

```python
    c = db.cursor()
```
- This line creates a cursor object named `c`. A cursor is used to execute SQL queries and fetch results from the database.

```python
    c.execute("SELECT * FROM `states`")
```
- This line executes an SQL query using the cursor. The query selects all columns (`*`) from the `states` table in the connected database.

```python
    [print(state) for state in c.fetchall()]
```
- This line uses a list comprehension to iterate through the result set obtained from executing the query. It fetches all rows using `c.fetchall()` and iterates through them, printing each row to the console using the `print()` function.

In summary, this script connects to a MySQL database, executes a query to select all states from a table called `states`, and then prints the results to the console. It takes three command-line arguments: the MySQL username, password, and database name, which are used to establish the database connection.

# ``filters state``
This Python script connects to a MySQL database and retrieves a list of states whose names start with the letter "N" from a table named "states." Here's an explanation of the code, followed by a sample output:

```python
#!/usr/bin/python3
"""
Lists all states with a name starting with N
"""
```

- This line is a shebang line that tells the system to use Python 3 to execute the script.
- The triple double-quotes `"""` are used for docstring comments to provide a brief description of what the script does.

```python
import sys
import MySQLdb
```

- The script imports two Python modules: `sys` for command-line arguments and `MySQLdb` for connecting to a MySQL database.

```python
if __name__ == '__main__':
```

- This condition checks if the script is being run as the main program (not imported as a module).

```python
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
```

- It establishes a database connection using the `MySQLdb.connect` function. The connection parameters (username, password, and database name) are provided through command-line arguments. `sys.argv` is a list that contains command-line arguments, with `sys.argv[0]` being the script name.

```python
    cur = db.cursor()
```

- This line creates a cursor object that allows you to interact with the database.

```python
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
```

- It executes a SQL query to select all rows from the "states" table and orders them by the "id" column.

```python
    states = cur.fetchall()
```

- The result of the query is fetched and stored in the `states` variable as a list of tuples, where each tuple represents a row from the "states" table.

```python
    [print(state) for state in states if state[1][0] == "N"]
```

- This is a list comprehension that iterates through the `states` list and prints the rows (states) whose name, accessed by `state[1]`, starts with the letter "N."

Sample Output (assuming the script is run with appropriate command-line arguments):

```
(4, 'New York')
(8, 'North Carolina')
(9, 'North Dakota')
```

# ``Filters state with user inpUt``
This Python script connects to a MySQL database and retrieves all rows from the "states" table where the name matches a specified argument. Here's an explanation of the code:

```python
#!/usr/bin/python3
# Displays all values in the states table of the database hbtn_0e_0_usa
# whose name matches that supplied as an argument.
# Usage: ./2-my_filter_states.py <mysql username> \
#                                <mysql password> \
#                                <database name> \
#                                <state name searched>
```

- This is a shebang line that specifies the script should be executed using Python 3. It also includes comments that provide a brief description of the script's purpose and usage.

```python
import sys
import MySQLdb
```

- The script imports two Python modules: `sys` for command-line arguments and `MySQLdb` for connecting to a MySQL database.

```python
if __name__ == "__main__":
```

- This condition checks if the script is being run as the main program (not imported as a module).

```python
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
```

- This line establishes a database connection using the `MySQLdb.connect` function. The connection parameters (username, password, and database name) are provided as command-line arguments.

```python
    c = db.cursor()
```

- It creates a cursor object (`c`) that allows you to interact with the database.

```python
    c.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))
```

- This line executes a SQL query to select all rows from the "states" table where the `name` column matches the argument provided as `sys.argv[4]`. The `BINARY` keyword ensures a case-sensitive comparison.

```python
    [print(state) for state in c.fetchall()]
```

- This list comprehension fetches all the matching rows returned by the query and prints them.

To use this script, you would run it from the command line with the following arguments:

```
./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>
```

It will connect to the specified database, execute the query, and print the matching rows from the "states" table.
