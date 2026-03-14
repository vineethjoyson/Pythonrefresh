import copy
import json
import math
import datetime
a="hello"
value=1.5
print(a)
print(f"the value is {value}")
list=["apple","pineApple","orannge","grapes"]
print(len(list))
users = [
    {"name": "Vineeth", "age": 28},
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30}
]
for user in users:
    print(user.get("name"))

#String Operations
data="hello Im vineeth"
print(data[:2])
print(data.upper())
print(data.lower())
print(data.title())
print(len(data))
print(data.find("hellos"))   # 0 when found, -1 when not found
newdata=data.replace("hello","hai")
print(newdata)

#list
newList=[1,2,3,4,5,6,7,8,9,10] #sorting inplace
newList.sort()
print(newList)
newList.sort(reverse=True)
print(newList)
#pushing =append
newList.append("helllo")
print(newList)
newList.pop()
print(newList)
numbers = [1,2,3]
numbers.extend([4,5,6]) # for adding multiple elements
print(numbers)
print(3 in numbers) # checking the list smae ase .includes
print(9 not in numbers)# for both return is a boolean
numbers.remove(1)
print(numbers)
newNum=numbers.copy()#copying a list
newNum.append("hellothere")
print(newNum)
print(numbers)
list1 = [[1,2],[3,4]]

list2 = copy.deepcopy(list1)
print(list2)

msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(csv.split(','))
print(''.join(friends_list))

print(''.join(msg.split()))
print(msg.replace(' ', ''))

#functions
def myFirstFunction(data):
    print(f"hello from my funvtion and its argument is {data}")
    return "hello there"
fnResp=myFirstFunction("argument")
print(fnResp)

#Named Notation
def greeting(name, age=28, color="red"):#default values
 #Greets user with “name” from “input box” and “age”, if unavailable, default age is used   
   
   print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
   print(f"We hear you like the color {color.lower()}!")

greeting(age=27, name="brian",color="Blue") #for readability we gave similar argumants

#Comparison
a=7
b=3
print('a == b is', a == b)
print('a != b is', a != b)
print('a > b is', a > b)
print('a < b is', a < b)
print('a >= b is', a >= b)
print('a <= b is', a <= b)
print('o in John is ','o' in 'John') #membership
print('o in John is ','o' not in 'John') #non membership
print('John is John ','John' is 'John') #identity
print('John is not John is ','John' is not 'John') # negative identity


#Conditional
is_raining = True
is_cold = True
print("Good Morning!")
if is_raining and is_cold: 
    print("Bring umbrella and jacket!")
elif is_raining and not(is_cold):
    print("Bring umbrella!")
elif not(is_raining) and is_cold:
    print("Bring jacket!")
else:
    print("Umbrella optional!")

def num_days(month):
    days = 31
    if (month.lower() in {'apr','jun','sep','nov'}): # here we use set because the lookup is more faster they use hasgh internally
    #if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in',month,'is',days)
    

num_days('jun')


# Loops 
i=0
while i <= 5:
    print(i)
    i += 1

for user in users:
    print(user.get("name"))

#Dictionaries
user = {
    "name": "Vineeth",
    "age": 28
}
print(user["name"])
print(user.get("name"))
user = {"name":"Vineeth","age":28}

user["city"] = "Kerala"

print(user.keys())
print(user.values())
print(user.items())

for key in user:
    print(key)

for value in user.values():
    print(value)


#error handlingError Handling
try:
    pass
except ValueError:
    pass
except Exception as e:
    print(e)
