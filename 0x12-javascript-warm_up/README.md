![js](https://i0.wp.com/hanamon.kr/wp-content/uploads/2021/12/javascript-logo.jpeg?resize=980%2C551&ssl=1)

# 0x12. JavaScript - Warm up

# Resurces  📑
[Writing JavaScript Code ](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
[Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
[Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
[Operators](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
[Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)
[Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
[Functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)
[Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
[Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
[Module pattern]
[var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)
[JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)
[Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)


# tasks 🚀

#return string 

```javascript
#!/usr/bin/node
```

This line is called a shebang, which is used to specify the interpreter for the script. It's correctly set to `/usr/bin/node` for Node.js.

```javascript
if (process.argv.length < 3) {
```

This line starts an `if` statement. It checks the length of the `process.argv` array, which contains command-line arguments. In the context of this script, it's checking if there are fewer than 3 arguments.

```javascript
console.log('No argument');
```

If there are fewer than 3 arguments, this line prints "No argument" to the console.

```javascript
} else if (process.argv.length === 3) {
```

This line starts an `else if` statement. It checks if there are exactly 3 arguments.

```javascript
console.log('Argument found');
```

If there are exactly 3 arguments, this line prints "Argument found" to the console.

```javascript
} else {
```

This line starts an `else` block, which executes if there are more than 3 arguments.

```javascript
console.log('Arguments found');
```

If there are more than 3 arguments, this line prints "Arguments found" to the console.

Your original code is correct and accomplishes the task as described in your initial request. It checks the number of command-line arguments and provides different output messages accordingly:

- If there are fewer than 3 arguments, it prints "No argument."
- If there are exactly 3 arguments, it prints "Argument found."
- If there are more than 3 arguments, it prints "Arguments found."


