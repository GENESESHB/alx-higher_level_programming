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
