class student:
    def __init__(self,name, age, number, gender,degree):
        self.name = name
        self.age = age
        self.gender = gender
        self.number = number
        self.degree = degree



    def ID(self):
        print(f"{self.name} isimli", f"{self.age} yasinda ", f"{self.number} numarali",f"{self.degree} .sinif ogrencimizdir" )
    

student1 = student("Elcin", 25, 6236362, "Kadin",5)

student.ID(self)