# 0x13-javascript_objects_scopes_closures

![js](https://biztecno.net/wp-content/uploads/2020/08/Biz-InfoTecno-Development-Full.png)
# Resources 📑

[ALL](https://intranet.alxswe.com/projects/304)

# Tasks 🚀✨

# empty class

```javascript
#!/usr/bin/node
module.exports = class Rectangle {};
```

This code creates an empty `Rectangle` class using ES6 syntax and exports it as a module. The shebang `#!/usr/bin/node` indicates that this file should be executed with Node.js.

You can save this code in a file, for example, "rectangle.js," and use it as a module in other JavaScript files by importing it with `require` like this:

```javascript
const Rectangle = require('./rectangle');

// Create instances of Rectangle and use them as needed.
const r1 = new Rectangle();
const r2 = new Rectangle();
```

Make sure to specify the correct path to the "rectangle.js" file based on its actual location on your system.

# vconstructor = attribute

`Rectangle` class with a constructor that accepts `width` and `height` parameters. This class allows you to create instances of rectangles with specific dimensions. Your code is correct for defining such a class.

Here's a breakdown of the code:

```javascript
#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
  }
};
```

- `#!/usr/bin/node`: This shebang indicates that the script should be executed using Node.js.

- `module.exports`: This line exports the `Rectangle` class as a module so that it can be used in other JavaScript files.

- `class Rectangle { ... }`: This is the class definition. It defines a `Rectangle` class with a constructor that takes two parameters, `w` (width) and `h` (height).

- Inside the constructor, `this.width = w;` and `this.height = h;` set the `width` and `height` properties of the instance to the values passed as arguments.

You can now create instances of the `Rectangle` class with specific dimensions like this:

```javascript
const Rectangle = require('./your-rectangle-file.js'); // Replace 'your-rectangle-file.js' with the actual filename.

const myRectangle = new Rectangle(10, 20); // Create a rectangle with width 10 and height 20.

console.log(myRectangle.width); // Output: 10
console.log(myRectangle.height); // Output: 20
```
# class and ``if`` statement


```javascript
#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }
};
```

This code defines a `Rectangle` class with a constructor that sets the `width` and `height` properties if both `w` and `h` are greater than 0. Let's create an example script that uses this class and prints out the properties:

```javascript
const Rectangle = require('./your-rectangle-file.js'); // Replace 'your-rectangle-file.js' with the actual filename.

const rect1 = new Rectangle(10, 20);
console.log(rect1.width); // Output: 10
console.log(rect1.height); // Output: 20

const rect2 = new Rectangle(-5, 30);
console.log(rect2.width); // Output: undefined
console.log(rect2.height); // Output: undefined
```

In the example above, we first create a `Rectangle` object `rect1` with valid dimensions (10 and 20), and it sets the `width` and `height` properties accordingly. Then, we create another `Rectangle` object `rect2` with dimensions that are not valid (-5 and 30), so the constructor does not set the properties, and they remain `undefined`;


# ``SQUARE`` & ``Rectangle``


```javascript
#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }
};
```

Now, let's create an example script that uses this class and prints out the rectangle:

```javascript
const Rectangle = require('./your-rectangle-file.js'); // Replace 'your-rectangle-file.js' with the actual filename.

const rect1 = new Rectangle(5, 3);
rect1.print();
```

The expected output when you run this script with `node` should be a rectangle made of "X" characters:

```
XXXXX
XXXXX
XXXXX
```

In this example, we create a `Rectangle` object `rect1` with dimensions 5 (width) and 3 (height), and then we call the `print` method to display the rectangle. The `print` method prints a rectangle with the specified dimensions, using "X" characters for the shape.

# SAUARE && ``rotate&double``

Your code defines a `Rectangle` class with additional methods `rotate` and `double` in addition to the existing `constructor` and `print` methods. Here's your code:

```javascript
#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }

  rotate() {
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
```

Now, let's create an example script that uses this extended class and demonstrates the `rotate` and `double` methods:

```javascript
const Rectangle = require('./your-rectangle-file.js'); // Replace 'your-rectangle-file.js' with the actual filename.

const rect1 = new Rectangle(5, 3);
console.log("Original:");
rect1.print();

rect1.rotate();
console.log("\nAfter Rotate:");
rect1.print();

rect1.double();
console.log("\nAfter Double:");
rect1.print();
```

The expected output when you run this script with `node` should be as follows:

```
Original:
XXXXX
XXXXX
XXXXX

After Rotate:
XXX
XXX
XXX
XXX
XXX

After Double:
XXXXXX
XXXXXX
XXXXXX
```

In this example, we create a `Rectangle` object `rect1` with dimensions 5 (width) and 3 (height). We then demonstrate the `rotate` and `double` methods. The `rotate` method swaps the `width` and `height`, and the `double` method doubles both the `width` and `height` of the rectangle. The `print` method is used to display the rectangle at each step.

# ||``inheritance`` = ``extends&super``

👨‍💻

```javascript
#!/usr/bin/node
module.exports = class Square extends require('./4-rectangle.js') {
  constructor(size) {
    super(size, size);
  }
};
```

And assuming that your `4-rectangle.js` module exports a `Rectangle` class with a `print` method, you can create a script to use the `Square` class and display the output. Here's an example:

**4-rectangle.js** (Assuming this is your `Rectangle` class)

```javascript
class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
```

**square.js** (Your script using the `Square` class)

```javascript
const Square = require('./your-square-file.js'); // Replace 'your-square-file.js' with the actual filename.

const square1 = new Square(5);
console.log("Square 1:");
square1.print();

const square2 = new Square(3);
console.log("\nSquare 2:");
square2.print();
```

The expected output when you run the `square.js` script with `node` should be as follows:

```
Square 1:
XXXXX
XXXXX
XXXXX
XXXXX
XXXXX

Square 2:
XXX
XXX
XXX
```

In this output, `square1` has a size of 5, and `square2` has a size of 3. The `print` method of the `Rectangle` class is used to display the squares.

# anather's methode `` for`` inhiretence

Here's the code:

```javascript
#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint(c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
};
```

This code defines a `Square` class that extends another class from the module `5-square.js`. It also includes a method called `charPrint(c)` that can be used to print a square made of a specific character `c`.

Let's break down the code:

1. `#!/usr/bin/node`: This is a shebang that indicates the script should be executed using Node.js.

2. `module.exports`: This line exports the `Square` class as a module so that it can be used in other JavaScript files.

3. `class Square extends require('./5-square.js')`: This line defines the `Square` class, which extends the class from the module `5-square.js`. This means that `Square` inherits the properties and methods of the class from the module.

4. Inside the `Square` class, there is a method called `charPrint(c)`. This method takes one parameter `c`, which represents the character to use when printing the square.

5. Inside the `charPrint` method, there is an `if` statement that checks if the `c` parameter is `undefined`. If `c` is not provided (undefined), it calls the `print` method of the parent class. If `c` is provided, it uses a loop to print a square made of the specified character `c` by repeating it `this.width` times on each line, for a total of `this.height` lines.

Now, let's create an example script that uses this `Square` class and demonstrates its `charPrint` method:

**Example Script (square.js):**

```javascript
const Square = require('./your-square-file.js'); // Replace 'your-square-file.js' with the actual filename.

const square1 = new Square(5);
console.log("Square 1:");
square1.charPrint();

const square2 = new Square(3);
console.log("\nSquare 2:");
square2.charPrint('*'); // Print square with '*' character
```

**Expected Output:**

```
Square 1:
XXXXX
XXXXX
XXXXX
XXXXX
XXXXX

Square 2:
***
***
***
```

In this example:

- `square1` is created with a size of 5. When you call `square1.charPrint()`, it uses the default character ('X') to print a square of size 5x5.

- `square2` is created with a size of 3. When you call `square2.charPrint('*')`, it prints a square of size 3x3 using the specified character ('*').

The `charPrint` method allows you to print squares with custom characters or use the default character ('X') if no character is provided.
