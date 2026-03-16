
# DRY (Don't Repeat Yourself)


class fruit:
    name = "fruits"

first = fruit()
print(first.name)

del first


class nothingE:
    pass



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"
    
    def greet(self):
        print(f"Hello, my name is {self.name}")

p1 = Person("John", 36)
p1.greet()

#self Does Not Have to Be Named "self"
#The __str__() method is a special method that controls what is returned when the object is printed:


#Child Class

class Student(Person):
  pass

#Python also has a super() function that will make the child class 
# inherit all the methods and properties from its parent:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


#In Python, you can make properties private by using a double underscore __ prefix:

#To access a private property, you can create a getter method:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())

#Private Methods. __brabra()