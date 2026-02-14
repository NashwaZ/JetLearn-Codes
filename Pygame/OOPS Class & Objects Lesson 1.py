# How to make a class

# A class in python is a blueprint for creating objects/instances
 
class Student():
    # Attributes/properties
    name = ""
    age = 12
    grade = 6
    house = "blue"
    class_teacher_name = "Ayushi"
    # Defining a constructor - a special method that gets called automatically when a a new instance/object of a class is created
    def __init__(self):
        print("Making a new student")
    def change_details(self):
        print("Please enter your name: ")
        self.name = input()
        print("Please enter your age: ")
        self.age = int(input())
    def show_details(self):
        print("Your name is: ", self.name)
        print("Your age is: ", self.age)
        print("You are in grade: ", self.grade)
        print('Your house is: ', self.house)
        print("Your class teacher is: ", self.class_teacher_name)
    def calculate_year_of_birth(self, current_year):
        year_of_birth = current_year - self.age
        return year_of_birth
    


# Objects/instances - is created from the class the class defines what properties and behaviors the objects will have.
# Making two objects of the Student class

Nashwa = Student()
Amirah = Student()
Ahlam = Student()


#Caling method show or change function (details)

Nashwa.change_details()
print(Nashwa.show_details())

current_year = 2024
birth_year = Nashwa.calculate_year_of_birth(current_year)
print(birth_year)


'''Amirah.change_details()
print(Amirah.show_details())

Ahlam.change_details()
print(Ahlam.show_details())'''

