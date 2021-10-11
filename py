Consider Python packages like Scikit-learn, pandas, and NumPy. These are all Python packages built with object-oriented programming.

OOP
Objects have characteristics (attributes) and actions (methods)

Class: A blueprint consisting of methods and attributes.
Object: An instance of a class.
Attribute: A descriptor or characteristic.
Method: An action that a class or object could take.
Encapsulation: One of the fundamental ideas behind object-oriented programming:
you can combine functions and data all into a single entity, called a class.
Encapsulation allows you to hide implementation details, much like how the scikit-learn package hides the implementation of machine learning algorithms.


A function and a method look very similar. They both use the def keyword.
They also have inputs and return outputs. The difference is that a method is inside of a class whereas a function is outside of a class.

class:
  def __innit__ (self, ):
  
  def (self, ):

Initialize an object in a class. Instatiate an object.
When you call a method, self is implicitly passed in.

In another .py file from first.py import class
Run code in terminal
  change directory cd
  python file.py
  
Changing values of an attribute directly(worse) or through a method(better):
A get method is for obtaining an attribute value. A set method is for changing an attribute value.
e.g.
class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self._price = shirt_price

    def get_price(self):
      return self._price

    def set_price(self, new_price):
      self._price = new_price
      
   Instantiating and using an object might look like the following code:

shirt_one = Shirt('yellow', 'M', 'long-sleeve', 15)
print(shirt_one.get_price())
shirt_one.set_price(10)

Docstrings example
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
