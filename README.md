# Python Basics Reference Guide

A personal quick-reference guide for common Python concepts including:

-   Variables
-   Strings
-   Lists
-   Dictionaries
-   Sets
-   Functions
-   Loops
-   Conditions
-   JSON
-   Error Handling
-   File Handling
-   Useful Built-in Modules

This document is intended as a **quick revision guide for backend
development and scripting**.

------------------------------------------------------------------------

# 1. Importing Modules

Python provides many built-in modules.

``` python
import copy
import json
import math
import datetime
```

## Common Modules

  Module     Purpose                  Example
  ---------- ------------------------ -------------------------
  copy       Copy objects             copy.deepcopy()
  json       Work with JSON data      json.loads()
  math       Mathematical functions   math.sqrt()
  datetime   Date and time            datetime.datetime.now()

Example:

``` python
import math
print(math.sqrt(16))
```

------------------------------------------------------------------------

# 2. Variables

Python variables are **dynamically typed**.

``` python
name = "Vineeth"
age = 28
price = 1.5
```

### f-Strings

``` python
print(f"My name is {name} and I am {age}")
```

------------------------------------------------------------------------

# 3. Strings

``` python
data = "hello Im vineeth"
```

## Common String Methods

  Method    Example
  --------- ----------------------------
  Slice     data\[:2\]
  Upper     data.upper()
  Lower     data.lower()
  Title     data.title()
  Length    len(data)
  Find      data.find("hello")
  Replace   data.replace("hello","hi")

Example:

``` python
print(data.upper())
print(data.lower())
print(data.replace("hello","hi"))
```

------------------------------------------------------------------------

# 4. Split and Join

## Split (String → List)

``` python
csv = "Eric,John,Michael"
print(csv.split(","))
```

## Join (List → String)

``` python
friends = ["Eric","John","Michael"]
print("".join(friends))
```

Remove spaces:

``` python
msg = "Welcome to Python 101"
print("".join(msg.split()))
```

------------------------------------------------------------------------

# 5. Lists

Lists are **ordered and mutable collections**.

``` python
fruits = ["apple","orange","grapes"]
```

## List Methods

  Method     Example
  ---------- ----------------------
  append()   list.append(x)
  pop()      list.pop()
  extend()   list.extend(\[4,5\])
  remove()   list.remove(x)
  copy()     list.copy()
  sort()     list.sort()

Example:

``` python
numbers = [1,2,3]
numbers.append(4)
numbers.extend([5,6])
print(numbers)
```

------------------------------------------------------------------------

# 6. Membership Operators

``` python
numbers = [1,2,3,4]
print(3 in numbers)
print(10 not in numbers)
```

Equivalent to JavaScript `.includes()`.

------------------------------------------------------------------------

# 7. Copying Lists

## Shallow Copy

``` python
new_list = numbers.copy()
```

## Deep Copy

``` python
import copy

list1 = [[1,2],[3,4]]
list2 = copy.deepcopy(list1)
```

------------------------------------------------------------------------

# 8. Dictionaries

Dictionaries store **key-value pairs**.

``` python
user = {
    "name": "Vineeth",
    "age": 28
}
```

## Access Values

``` python
print(user["name"])
print(user.get("name"))
```

## Dictionary Methods

  Method     Example
  ---------- --------------------
  keys()     dict.keys()
  values()   dict.values()
  items()    dict.items()
  update()   dict.update({...})
  pop()      dict.pop("key")

Example:

``` python
user["city"] = "Kerala"
print(user.keys())
print(user.values())
```

------------------------------------------------------------------------

# 9. Looping Through Dictionary

``` python
for key in user:
    print(key)

for value in user.values():
    print(value)

for key,value in user.items():
    print(key,value)
```

------------------------------------------------------------------------

# 10. List of Dictionaries

``` python
users = [
    {"name":"Vineeth","age":28},
    {"name":"John","age":25},
    {"name":"Alice","age":30}
]

for user in users:
    print(user.get("name"))
```

------------------------------------------------------------------------

# 11. Functions

``` python
def greet(name):
    print(f"Hello {name}")

greet("Vineeth")
```

------------------------------------------------------------------------

# 12. Default Parameters

``` python
def greeting(name, age=28, color="red"):
    print(f"Hello {name}, next year you will be {age+1}")
```

------------------------------------------------------------------------

# 13. Comparison Operators

  Operator   Meaning
  ---------- ------------------
  ==         equal
  !=         not equal
  \>         greater
  \<         less
  \>=        greater or equal
  \<=        less or equal

------------------------------------------------------------------------

# 14. Membership vs Identity

Membership:

``` python
'o' in 'John'
```

Identity:

``` python
x is None
```

------------------------------------------------------------------------

# 15. Conditional Statements

``` python
if condition:
    pass
elif condition:
    pass
else:
    pass
```

Example:

``` python
is_raining = True
is_cold = True

if is_raining and is_cold:
    print("Bring umbrella and jacket")
```

------------------------------------------------------------------------

# 16. Sets

``` python
months = {"apr","jun","sep","nov"}

if "apr" in months:
    print("30 days")
```

------------------------------------------------------------------------

# 17. Loops

## For Loop

``` python
for i in range(5):
    print(i)
```

## While Loop

``` python
i = 1
while i <= 5:
    print(i)
    i += 1
```

------------------------------------------------------------------------

# 18. JSON Handling

``` python
import json

data = '{"name":"Vineeth","age":28}'

user = json.loads(data)
print(user["name"])
```

Convert dictionary to JSON:

``` python
json_string = json.dumps(user)
```

------------------------------------------------------------------------

# 19. Error Handling

``` python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

------------------------------------------------------------------------

# 20. File Handling

## Read File

``` python
with open("file.txt","r") as f:
    data = f.read()
```

## Write File

``` python
with open("file.txt","w") as f:
    f.write("Hello world")
```

------------------------------------------------------------------------

# 21. Common Data Structures

  Type         Example
  ------------ --------------------
  List         \[1,2,3\]
  Dictionary   {"name":"Vineeth"}
  Set          {1,2,3}
  Tuple        (1,2,3)

------------------------------------------------------------------------

# 22. Useful Built-in Functions

  Function   Description
  ---------- -------------------
  len()      length
  type()     type of variable
  range()    generate sequence
  sum()      sum elements
  max()      maximum
  min()      minimum

Example:

``` python
numbers = [1,2,3,4]

print(sum(numbers))
print(max(numbers))
```

------------------------------------------------------------------------

# Author

Vineeth Joyson\
Python Learning Notes
