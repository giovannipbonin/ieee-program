# Week 5: Classes and Error Handling
1. Object-Oriented Programming 101
1. Thinking about creating new _types_
1. Dealing with what happens when your code goes bad
    - Errors and what to do about them

## Some Updates
1. Check out [Coursera's Python Sequence](https://www.coursera.org/specializations/python)
    - It's great to learn a language from a couple of different perspectives
1. Fun stuff: Go read some of Paul Graham's Essays
    - http://www.paulgraham.com/love.html
1. Python Practice
    - [Google Python Exercises](https://github.com/2gotgrossman/google-python-exercises)


## The Rest of the Semester
We've got 4 classes left. What did we agree on covering?
#### The "Musts"
1. Iterators and Generators AND Functional Python (`map`, `reduce`)

#### The Fun Ones
1. `pandas` - data manipulation and data analysis
1. `matplotlib` - data visualization
1. Intro to Machine Learning in Python
1. Programming challenges / Projects

## Last Week
1. Ways to think about program efficiency
    - Thinking about how much time and memory programs take up
1. Common data structures and their efficiency
1. A basic understanding is important to write Python code (or code in general) that doesn't run super slow

# Object-Oriented Programming
![Python Classes Meme](https://i.imgur.com/Cb3gD0G.jpg)
1. I borrow heavily from Jeff Knupp. Great post, would recommend you read it in addition to this (and also see how much I borrowed from him)
    - https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
1. Also, official Python3 tutorial on classes
    - https://docs.python.org/3/tutorial/classes.html

## Classes
1. `class` keyword
    - Like `def` defines a function, `class` defines _things_
        - Think data, ways of representing real work things, etc
    - Creates what is called a Class
        - Think _class_ify, not _class_room
1. A Class is a grouping of data (variables) and functions
1. Classes are oftentimes based on objects in the real world

## Objects
1. Classes and objects are not interchangeable
1. Classes are _blueprints for creating objects_
1. Defining a `class` doesn't "create" anything.
1. Objects are _instances_ of a class.
    - Think about zoology: We can define the characteristics of a dog (the class) without creating [Buddy](https://gbgrr.org/wp-content/uploads/Home-page-donate.jpg) (an object)

## `Customer` Example
1. Defining a customer class using the `class` keyword doesn't actual create a customer.
1. Instead, it creates an instruction manual for constructing "Customer" objects

```python
class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance
```

1. To create an _instance_ of a customer, we call the class's _init_ method with the arguments
    - `jeff = Customer('Jeff Knupp', 1000.0)`
        - Use the `Customer` blueprint to create me a new object, which I'll refer to as `jeff`
        - `jeff` is an _instance_ of the `Customer` _class_.

## `self`
1. `self` refers to the instance (the object that we are dealing with)
1. `jeff.withdraw(100.0)` calls the `withdraw` function on the `jeff` instance (modifies the `jeff` object, not the `marianne` object if we had one)
    - Shorthand for `Customer.withdraw(jeff, 100.0)`
        - Perfectly valid alternative

## `__init__`
1. The method to create an object
    - Used when you write `Customer("Jeff Knupp", 1000.0)`

## Static vs. Dynamic Methods
1. Some properties are shared amongst all objects of a class
    - These shared properties are called static

```python
class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model
    @staticmethod
    def make_car_sound():
        print 'VRooooommmm!'
```

## Inheritance
1. To learn on your own
    - A way to say that a `Tesla` is a type of `Car` and can "inherit" all the properties and methods from the `Car` class, but also have more

## Real Life Examples
1. When we were doing API REST Requests, we got something called a `Response` object back.
    - The `requests` module defined a _class_ called `Response` and calling `requests.get()` returns an _instance_ of the `Response` _class_.

```python
import requests


response = requests.get('http://api.open-notify.org/iss-now.json')
print("Status Code:", response.status_code) # a property of the `Response` class
```

# Errors
![Python Exceptions Meme](https://pbs.twimg.com/media/C4IO637WIAAHJIS.jpg:large)
1. When code fails (or it does something it's not supposed to), it will let you know with an error
1. **Errors before program execution** 
    - Caught before the program actually runs
    - Oftentimes syntax errors 
1. **Exceptions** are errors caught while a program is running
1. Common examples
    - `print( 5 + 1/0)`
        - `ZeroDivisionError`
    - ` list_of_numbers[ len(list_of_numbers) + 1]`
        - `IndexError`

## Handling Exceptions
1. But shtuff happens. We need to be able to deal with these errors without our program crashing
1. `try`-`except` statements!
1. Try this block of code:

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```
1. You can be general in your type of exceptions
    - Exceptions are Objects!

## The `Exception` class and `raise`ing your own errors
1. All exceptions inherit from the `Exception` class
1. You can (1) create your own exceptions by creating a class that inherits from this class or using this class itself

```python
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)
```
1. Output:
```
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```
1. In this case we handle our own exception. But sometimes, you might not want to handle your own exception! 
    - Let someone else handle your exception or let it stop program execution
    - Writing good exceptions can help you debug your code

## `try`, `except`, `else`, `finally`
1. `try` will attempt to execute the code in that block
2. `except` will handle specified errors
3. `else` will handle the case when no error is raised
4. `finally` will be executed after the `try` block no matter what!
```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
```

# Exercises!
1. Design a deck of cards.
