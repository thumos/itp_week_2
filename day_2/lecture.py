# ITP Week 2 Day 2 Lecture

# "Computer functions are similar to math functions in that they may reference parameters, which are passed, or input into the function."

#Use the "def" keyword to define (create) a new function.  Give the function a name, followed by single braces, and a colon.  Indent the following line to run the code in the function body.  The following code will create a function named myNewFunction, and it will print the words "Hello World"

def my_old_function():
    print("Hello")

# "Call" the function to run the code by adding single braces after the name of the function.

my_old_function()

#Functions can accept values and process them in different ways.

#A parameter represents a value that the procedure expects you to pass when you call it. The procedure's declaration defines its parameters.

#An argument represents the value that you pass to a procedure parameter when you call the procedure. The calling code supplies the arguments when it calls the procedure.

def my_new_function(parameter):
    print(parameter)

my_new_function("This is my Argument")

#Functions can have multiple parameters.

def multi_parameter(param1, param2, param3):
    print("My name is " + param1 + " " + param2 + ", and I live in " + param3 + ".")

multi_parameter("Tyler", "Pritchard", "Oakland")