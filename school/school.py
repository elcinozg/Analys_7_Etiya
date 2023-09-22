from student import student
from teacher import teacher


class school(student,teacher):
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
