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
