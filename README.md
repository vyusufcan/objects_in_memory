# objects_in_memory

In Python, everything is object

When object is created , object is stored in memory

a = [1,2,3,4,5]

Memory -> a ( and also a object has a memory id)

Id represents memory localtion for object

Programs keep track of how many "references" to the object exist

# Reference 

Name that refers to the location in memory of an object

Reference -> Variables, Attributes, Items

Variables in Python store references to objects in memory

When, there are no references to the object in the program, the object is deleted from memory

This is called Gargage Collection

# Object vs. Instance

You can think of objects as the "physical" existence of the instance in memory, the data that is stored in memory
to represent the instances, while instances represent a more theoretical cencept. A specific house object represent an instance of the House class in memory

# id() function

This function returns the address of the object in memory

# is operator

The operators is and is not test for an object's identity: x is y is true and only if x and y are the same object.
an object's identity is determined using the id() function. x is not y yields the inverse truth value

If two variables do not reference the same object, they will have different ids.
If two variables reference the same object, they will have the same id.

Returns True if both operands reference the same object. Else, it returns False

is -- > Checks the objects
== -- > Checks the values

Two objects may have the same value and still be different objects in memory

For certain values, the result might not be what we initially expect

# Unecpected Results

The current implementation keeps an array of integer objects for all integers between -5 and 256, when you create an int in that range you actually just get back a reference to the existing objects

# String Interning

Strings are immutable, so they cannot ve changed
The process of keeping only one distinct copy of the string in memory