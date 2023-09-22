class student:
    def __init__(self,name, age, number, gender,degree):
        self.name = input(" Ogrencinin ismi yaziniz: ")
        self.age = int(input("Ogrencinin yasini giriniz:  "))
        self.gender = input("Cinsiyet giriniz: ")
        self.number = int(input("Ogrenci numarasi giriniz: "))
        self.degree = int(input("Ogrencinin kacinci sinif oldugunu giriniz: "))


    def ID(self):
        print(f"{self.name} isimli", f"{self.age} yasinda ", f"{self.number} numarali",f"{self.degree} .sinif ogrencimizdir" )
    