# ITP Week 2 Day 3 Lecture

# The Python return statement is a key component of functions and methods. You can use the return statement to make your functions send Python objects back to the caller code. These objects are known as the function’s return value. You can use them to perform further computation in your programs.  The Python return statement is a special statement that you can use inside a function or method to send the function’s result back to the caller. A return statement consists of the return keyword followed by an optional return value.

# In general, a function takes arguments (if any), performs some operations, and returns a value (or object). The value that a function returns to the caller is generally known as the function’s return value. All Python functions have a return value, either explicit or implicit.

# An explicit return statement immediately terminates a function execution and sends the return value back to the caller code. 

# A Python function will always have a return value. There is no notion of procedure or routine in Python. So, if you don’t explicitly use a return value in a return statement, or if you totally omit the return statement, then Python will implicitly return a default value for you. That default return value will always be None.

# You can use a return statement to return multiple values from a function. To do that, you just need to supply several return values separated by commas.

# Functions can take lists and dictionaries as arguments. 

#Remember DRY (Do not repeat yourself!).  If you find yourself repeating code, assign that code to a variable and then simply use the variable where ever you would have written that function.

#You can import modules and get access to new functions.

# The modules that come with Python are called the standard library, but you can also install third-party modules using the pip tool.

# The sys.exit() function will immediately quit your program.

# The Pyperclip third-party module has copy() and paste() functions for reading and writing text to the clipboard().