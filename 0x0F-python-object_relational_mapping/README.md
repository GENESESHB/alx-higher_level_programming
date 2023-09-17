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

# ``SQL Injection...``

#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )

        # Create a cursor object
        cursor = db.cursor()

        # Prepare the SQL query using placeholders to avoid SQL injection
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        # Execute the query with the provided state_name
        cursor.execute(query, (state_name,))

        # Fetch all rows
        results = cursor.fetchall()

        # Display the results
        for row in results:
            print(row)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

# ``Cities by states``
To list all cities from the database `hbtn_0e_4_usa`, you can use the `MySQLdb` module in Python. Here's a script (`4-cities_by_state.py`) that accomplishes this task:

```python
#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )

        # Create a cursor object
        cursor = db.cursor()

        # Prepare the SQL query
        query = "SELECT cities.id, cities.name, states.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 ORDER BY cities.id ASC"

        # Execute the query
        cursor.execute(query)

        # Fetch all rows
        results = cursor.fetchall()

        # Display the results
        for row in results:
            print(row)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
```

Make sure the script is executable:

```bash
chmod +x 4-cities_by_state.py
```

You can then run the script with the following command:

```bash
./4-cities_by_state.py root root hbtn_0e_4_usa
```

This script connects to the MySQL server, retrieves data from the `cities` and `states` tables, and displays the results as specified in the example.

# ``ALL cities by state``

To create a script that lists all cities of a given state from the database `hbtn_0e_4_usa`, you can use the `MySQLdb` module in Python. Here's a script (`5-filter_cities.py`) that accomplishes this task safely, without SQL injection:

```python
#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )

        # Create a cursor object
        cursor = db.cursor()

        # Prepare the SQL query with a placeholder for the state_name
        query = "SELECT cities.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s \
                 ORDER BY cities.id ASC"

        # Execute the query with the provided state_name
        cursor.execute(query, (state_name,))

        # Fetch all rows
        results = cursor.fetchall()

        # Extract city names and join them with commas
        city_names = ', '.join(row[0] for row in results)

        # Display the results
        print(city_names)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
```

Make sure the script is executable:

```bash
chmod +x 5-filter_cities.py
```

You can then run the script with the following command, providing the state name as an argument:

```bash
./5-filter_cities.py root root hbtn_0e_4_usa Texas
```

This script connects to the MySQL server, retrieves the city names for the specified state, and displays them as a comma-separated list, as shown in the example.

# ``First state model``

#!/usr/bin/python3
"""Start link class to table in database 
"""

# `` First state model``

Certainly! Let's break down the code in `model_state.py` step by step:

```python
#!/usr/bin/python3
"""Start link class to table in database 
"""
```

- This is a shebang line (`#!/usr/bin/python3`) that specifies the interpreter to be used when executing the script.
- The triple double-quotes `"""` indicate a docstring, which is a way to provide documentation or comments about the code. In this case, it provides a brief description of the purpose of the script.

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
```

- These lines import necessary modules and classes from SQLAlchemy, a popular Object-Relational Mapping (ORM) library for Python.
- `Column`, `Integer`, and `String` are classes from SQLAlchemy used to define database table columns and their data types.
- `declarative_base` is a function from SQLAlchemy that creates a base class for declarative class definitions.

```python
Base = declarative_base()
```

- Here, we create a `Base` instance by calling `declarative_base()`. This `Base` instance will be used as a base class for all the declarative class definitions in our SQLAlchemy models.

```python
class State(Base):
    """Class that defines a State table"""
    __tablename__ = 'states'
```

- We define a Python class named `State` that inherits from the `Base` class. This class represents a table in the database.
- The `__tablename__` attribute is used to specify the name of the table in the database. In this case, it's set to 'states'.

```python
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
```

- Inside the `State` class, we define two class attributes: `id` and `name`.
- `id` is defined as a `Column` of type `Integer`, and it's set as the primary key of the table using `primary_key=True`. It's also set as not nullable using `nullable=False`, meaning it must have a value for every row. `autoincrement=True` indicates that this column is auto-incremented.
- `name` is defined as a `Column` of type `String(128)` (a string with a maximum length of 128 characters). It's also set as not nullable.

This code defines a SQLAlchemy model for a 'states' table, specifying the structure of the table and its columns. It's a declarative way to define the database schema in Python code, making it easier to work with databases using object-oriented programming principles

# ``All states via SQLAlchemy``.

Certainly! Let's go through the code step by step:

1. Importing necessary modules and classes:
```python
#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
```
   - This code starts with a shebang (`#!/usr/bin/python3`) to specify that the script should be executed using Python 3.
   - It imports the required modules: `sys`, `create_engine`, `sessionmaker`, and the classes `Base` and `State` from the `model_state` module.

2. Checking if the script is the main program:
```python
if __name__ == "__main__":
```
   - This conditional statement ensures that the following code block is only executed if this script is run as the main program, not when it's imported as a module.

3. Retrieving command-line arguments:
```python
    # Get command-line arguments
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
```
   - It retrieves the command-line arguments using `sys.argv`. The first argument (`sys.argv[0]`) is the script's filename, so `sys.argv[1]`, `sys.argv[2]`, and `sys.argv[3]` correspond to the MySQL username, password, and database name provided when running the script.

4. Creating a database engine and session:
```python
    # Create a database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(db_username, db_password, db_name),
                           pool_pre_ping=True)
```
   - This code uses the `create_engine` function from SQLAlchemy to create a database engine. It uses the provided username, password, and database name to specify the database connection URL. The `pool_pre_ping=True` option ensures that the database connection is refreshed if it becomes stale.

5. Creating a session:
```python
    # Create an SQLAlchemy session
    Session = sessionmaker(bind=engine)
    session = Session()
```
   - It creates an SQLAlchemy `Session` class tied to the previously created database engine and then creates an actual session object.

6. Querying the database for State objects:
```python
    # Query the database to retrieve all State objects, ordered by their IDs
    states = session.query(State).order_by(State.id).all()
```
   - This code uses the session to query the database and retrieve all `State` objects from the database table. The `order_by(State.id)` part ensures that the results are sorted by the `id` column in ascending order.

7. Displaying the results:
```python
    # Display the results
    for state in states:
        print("{}: {}".format(state.id, state.name))
```
   - It iterates through the retrieved `State` objects and prints their `id` and `name` attributes.

8. Closing the session:
```python
    # Close the session
    session.close()
```
   - Finally, it closes the session to release resources and close the database connection.

This script essentially connects to a MySQL database, retrieves a list of `State` objects, and prints them in ascending order by their IDs. It's a basic example of how to use SQLAlchemy to interact with a database in Python
.

# ``First state``

Certainly! Let's go through the code line by line and explain each part along with the expected output.

```python
#!/usr/bin/python3
```

- This is a shebang line specifying that the script should be executed using the Python 3 interpreter.

```python
import sys
```

- This line imports the `sys` module, which provides access to command-line arguments and other system-related functions.

```python
from model_state import Base, State
```

- This line imports the `Base` and `State` classes from the `model_state` module. These classes are part of SQLAlchemy's ORM (Object-Relational Mapping) and represent the database tables.

```python
from sqlalchemy import create_engine
```

- This line imports the `create_engine` function from the SQLAlchemy library, which is used to create a connection to the database.

```python
from sqlalchemy.orm import sessionmaker
```

- This line imports the `sessionmaker` function from SQLAlchemy's ORM, which is used to create a configured "Session" class for interacting with the database.

```python
if __name__ == "__main__":
```

- This conditional block checks if the script is being run as the main program.

```python
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
```

- This part checks if the script is provided with the correct number of command-line arguments (4 in total: script name, username, password, and database name). If not, it prints a usage message and exits the script with a status code of 1.

```python
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
```

- These lines retrieve the values of the username, password, and database name from the command-line arguments.

```python
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database), pool_pre_ping=True)
```

- Here, an SQLAlchemy engine is created using the `create_engine` function. It specifies the connection URL to the MySQL database with the provided username, password, and database name. The `pool_pre_ping=True` argument enables connection pooling with ping for reconnections.

```python
    Session = sessionmaker(bind=engine)
    session = Session()
```

- These lines create an SQLAlchemy session using the `sessionmaker` function and bind it to the previously created engine. This session will be used for database interactions.

```python
    first_state = session.query(State).order_by(State.id).first()
```

- This line queries the database using the session to retrieve the first `State` object. The `order_by(State.id)` part ensures that the results are sorted in ascending order by the `id` column.

```python
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
```

- This part checks if a `first_state` object was found in the database. If a `State` object is found, it prints its `id` and `name` in the specified format. If no `State` object is found (the table is empty), it prints "Nothing."

```python
    session.close()
```

- Finally, the script closes the session to release the resources associated with it.

Expected Output (example):

Let's assume you run the script with the following command:

```bash
./8-model_state_fetch_first.py root root hbtn_0e_6_usa
```

- If there is a `State` object in the database, it will print something like:
  ```
  1: California
  ```

- If there are no `State` objects in the database (empty table), it will print:
  ```
  Nothing
  ```

The actual output will depend on the contents of the database and the provided command-line arguments.

