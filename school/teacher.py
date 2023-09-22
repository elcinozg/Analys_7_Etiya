class teacher:
    def __init__(self,name, age, branch, salary, gender):
        self.name = input("Ogretmenin ismini yaziniz: ")
        self.age = int(input("Ogretmenin yasini giriniz:  "))
        self.branch = input("Ogretmenin bransini giriniz: ")
        self.salary = int(input("Maas giriniz: "))
        self.gender = input("Cinsiyet giriniz: ")

    def ID(self):
        print(f"{self.name} isimli", f"{self.age} yasinda ", f"{self.branch} bransinda ders vermektedir. ")

    


    
