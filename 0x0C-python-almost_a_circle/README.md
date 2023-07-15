# 0x0C-python-almost_a_circle


# =>>the first class Base:

  ```Here's the complete code:
  ```

```python
#!/usr/bin/python3
"""Defines a base model class."""

class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
```

This code defines a base model class named `Base` with a class variable `__nb_objects` and an initializer method `__init__`. The class variable `__nb_objects` keeps track of the number of instantiated `Base` objects, and the `__init__` method assigns unique identifiers to each object.

Note that this code assumes it is part of a module and does not include a `main` section or demonstrate the usage of the `Base` class.


# =>the class Rectangle that inherits from Base:

```in this tasks we have initialisation a new rectangle and we wanna a id() for rectangle that maens we imports the models of class Base: because he hase a difination of id() and we use the By calling super().__init__(id), the Rectangle class inherits and utilizes the initialization logic defined in the __init__ method of the Base class. This allows the Rectangle class to benefit from any common setup or shared functionality provided by the Base class.
```

To implement the `Rectangle` class that inherits from `Base` and includes private instance attributes with getters and setters, you can create a new file called `rectangle.py` inside the `models` directory. Here's an example implementation:

```python
#!/usr/bin/python3
"""Defines the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): The identity of the new Rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        self.__y = value
```

In this code, the `Rectangle` class inherits from the `Base` class, and the private instance attributes (`__width`, `__height`, `__x`, and `__y`) have their own getters and setters defined using the `@property` decorator.

The constructor (`__init__`) initializes the `Rectangle` object by calling the superclass constructor (`super().__init__(id)`) and assigns the values of the provided arguments to the corresponding attributes (`width`, `height`, `x`, and `y`).

The getters and setters provide controlled access to the private attributes, allowing validation or additional logic to be implemented if needed.

The provided `main.py` script demonstrates how to use the `Rectangle` class by creating instances and printing their IDs.
